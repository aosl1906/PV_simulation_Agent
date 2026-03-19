"""
Module: src/mcp_server.py

Beschreibung:
    MCP Server für das PV Simulation Tool.
    Exponiert das bestehende PV Simulation Backend als MCP-Tools
    für KI-Agenten (Antigravity, Claude Desktop, etc.).

    Der Server selbst enthält kein LLM — er ist ein reiner Adapter,
    der MCP-Tool-Aufrufe in HTTP-Requests an das PV Backend übersetzt.

Starten:
    python src/mcp_server.py

MCP Client Konfiguration:
    {
        "mcpServers": {
            "pv-simulation": {
                "command": "python",
                "args": ["D:/Antigravity/PV_simulation_Agent/src/mcp_server.py"]
            }
        }
    }
"""
import sys
import os
import json
import logging

# Projekt-Root zum Python-Path hinzufügen (damit src.* Imports funktionieren)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from dotenv import load_dotenv
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

from fastmcp import FastMCP
from src.tools.simulate import build_simulation_request, run_simulation, format_summary
from src.tools.geocode import geocode_address as _geocode

# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)
logger = logging.getLogger("mcp.server")

# --- MCP Server Instanz ---
mcp = FastMCP(
    "PV Simulation Agent",
    instructions=(
        "Dieser MCP Server bietet Zugriff auf ein PV-Simulationstool. "
        "Du kannst damit Photovoltaik-Anlagen simulieren, inklusive "
        "Batterie, Wärmepumpe, E-Auto und Smart-Home-Optimierung. "
        "Schritt 1: Nutze geocode_address um Koordinaten für den Standort zu erhalten. "
        "Schritt 2: Nutze simulate_project mit den Koordinaten und PV-Konfiguration. "
        "Die Ergebnisse enthalten Jahresertrag, Autarkie, Eigenverbrauch und Wirtschaftlichkeit."
    ),
)


# ============================================================
# Tool 1: get_simulation_schema
# ============================================================
@mcp.tool
def get_simulation_schema() -> str:
    """
    Gibt das JSON-Schema für eine PV-Simulationsanfrage zurück.
    Nutze dieses Schema um zu verstehen, welche Parameter möglich sind.

    Die wichtigsten Parameter sind:
    - latitude/longitude: Standort (nutze geocode_address um diese zu erhalten)
    - arrays: Liste der PV-Module mit tilt (Neigung), azimuth (Ausrichtung), peak_power_kw
    - battery_params: Batteriespeicher (optional)
    - consumption_params: Stromverbrauch
    - heat_pump_params: Wärmepumpe (optional)
    - wallbox_params: E-Auto Wallbox (optional)
    - hems_params: Smart Home Optimierung (optional)
    - economics_params: Strompreis und Einspeisevergütung
    """
    schema_path = os.path.join(PROJECT_ROOT, "schemas", "simulation_schema.json")
    if os.path.exists(schema_path):
        with open(schema_path, "r", encoding="utf-8") as f:
            return f.read()

    # Fallback: Inline-Schema der wichtigsten Parameter
    return json.dumps({
        "description": "SimulationRequest — Wichtigste Parameter",
        "required": ["latitude", "longitude", "arrays"],
        "properties": {
            "latitude": {"type": "number", "description": "Breitengrad"},
            "longitude": {"type": "number", "description": "Längengrad"},
            "arrays": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "default": "PV Array"},
                        "tilt": {"type": "number", "default": 30, "description": "Neigung in Grad (0=flach, 90=senkrecht)"},
                        "azimuth": {"type": "number", "default": 180, "description": "Ausrichtung in Grad (0=N, 90=O, 180=S, 270=W)"},
                        "peak_power_kw": {"type": "number", "description": "Nennleistung in kWp"},
                    },
                },
            },
            "battery_params": {
                "type": "object",
                "properties": {
                    "capacity_kwh": {"type": "number", "default": 0},
                    "max_charge_kw": {"type": "number", "default": 5},
                    "max_discharge_kw": {"type": "number", "default": 5},
                },
            },
            "consumption_params": {
                "type": "object",
                "properties": {
                    "annualKwh": {"type": "number", "default": 4500},
                    "type": {"type": "string", "enum": ["family", "single", "couple"], "default": "family"},
                },
            },
        },
    }, indent=2, ensure_ascii=False)


# ============================================================
# Tool 2: geocode_address
# ============================================================
@mcp.tool
async def geocode_address(address: str) -> str:
    """
    Wandelt eine Adresse oder einen Stadtnamen in Koordinaten (Breitengrad/Längengrad) um.
    Nutze dieses Tool ZUERST, bevor du eine Simulation startest.

    Beispiele:
    - "München"
    - "Musterstraße 1, 80331 München"
    - "Stuttgart, Deutschland"

    Args:
        address: Freitext-Adresse oder Stadtname

    Returns:
        JSON mit latitude, longitude und display_name
    """
    result = await _geocode(address)

    if "error" in result:
        return f"❌ {result['error']}"

    return json.dumps({
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "display_name": result["display_name"],
    }, indent=2, ensure_ascii=False)


# ============================================================
# Tool 3: simulate_project
# ============================================================
@mcp.tool
async def simulate_project(
    latitude: float,
    longitude: float,
    peak_power_kw: float,
    tilt: float = 30.0,
    azimuth: float = 180.0,
    battery_capacity_kwh: float = 0.0,
    annual_consumption_kwh: float = 4500.0,
    heat_pump_enabled: bool = False,
    heat_pump_annual_demand_kwh: float = 10000.0,
    wallbox_enabled: bool = False,
    wallbox_daily_km: float = 40.0,
    wallbox_charge_power_kw: float = 11.0,
    hems_enabled: bool = False,
    electricity_price_eur: float = 0.30,
    feed_in_tariff_eur: float = 0.08,
) -> str:
    """
    Führt eine vollständige PV-Simulation durch und gibt die Ergebnisse zurück.

    Nutze ZUERST geocode_address um die Koordinaten zu bestimmen.

    Die Simulation berechnet für ein ganzes Jahr (8760 Stunden):
    - PV-Ertrag basierend auf Standort, Ausrichtung und Neigung
    - Eigenverbrauch und Netzeinspeisung
    - Autarkiegrad
    - Batterie-Nutzung (falls konfiguriert)
    - Wärmepumpe und E-Auto Auswirkungen (falls aktiviert)
    - Wirtschaftlichkeit (Ersparnis, Amortisation)

    Args:
        latitude: Breitengrad (z.B. 48.14 für München)
        longitude: Längengrad (z.B. 11.58 für München)
        peak_power_kw: PV-Nennleistung in kWp (z.B. 10.0)
        tilt: Dachneigung in Grad (0=flach, 30=Standard, 90=senkrecht). Default: 30
        azimuth: Ausrichtung in Grad (0=Nord, 90=Ost, 180=Süd, 270=West). Default: 180 (Süd)
        battery_capacity_kwh: Batteriespeicher in kWh (0=keine Batterie). Default: 0
        annual_consumption_kwh: Jahresstromverbrauch in kWh. Default: 4500
        heat_pump_enabled: Wärmepumpe vorhanden? Default: False
        heat_pump_annual_demand_kwh: Jährlicher Wärmebedarf in kWh. Default: 10000
        wallbox_enabled: E-Auto Wallbox vorhanden? Default: False
        wallbox_daily_km: Tägliche Fahrtstrecke in km. Default: 40
        wallbox_charge_power_kw: Ladeleistung der Wallbox in kW. Default: 11
        hems_enabled: Smart Home Optimierung aktivieren? Default: False
        electricity_price_eur: Strompreis in €/kWh. Default: 0.30
        feed_in_tariff_eur: Einspeisevergütung in €/kWh. Default: 0.08
    """
    # PV Array bauen (Phase 1: ein Array, später mehrere)
    arrays = [{
        "name": f"PV Array ({peak_power_kw:.1f} kWp)",
        "tilt": tilt,
        "azimuth": azimuth,
        "peak_power_kw": peak_power_kw,
    }]

    # SimulationRequest bauen
    request = build_simulation_request(
        latitude=latitude,
        longitude=longitude,
        arrays=arrays,
        battery_capacity_kwh=battery_capacity_kwh,
        annual_consumption_kwh=annual_consumption_kwh,
        heat_pump_enabled=heat_pump_enabled,
        heat_pump_annual_demand_kwh=heat_pump_annual_demand_kwh,
        wallbox_enabled=wallbox_enabled,
        wallbox_daily_km=wallbox_daily_km,
        wallbox_charge_power_kw=wallbox_charge_power_kw,
        hems_enabled=hems_enabled,
        electricity_price_eur=electricity_price_eur,
        feed_in_tariff_eur=feed_in_tariff_eur,
    )

    # Simulation ausführen
    result = await run_simulation(request)

    if "error" in result:
        return f"❌ {result['error']}"

    return result["summary_text"]


# ============================================================
# Tool 4: check_backend_status
# ============================================================
@mcp.tool
async def check_backend_status() -> str:
    """
    Prüft ob das PV Simulation Backend erreichbar ist.
    Nützlich zur Diagnose, falls Simulationen fehlschlagen.
    """
    from src.utils.http_client import check_backend_health, get_backend_url

    url = get_backend_url()
    healthy = await check_backend_health()

    if healthy:
        return f"✅ PV Simulation Backend erreichbar unter {url}"
    else:
        return (
            f"❌ PV Simulation Backend NICHT erreichbar unter {url}\n"
            f"Bitte sicherstellen, dass das Backend gestartet ist.\n"
            f"Start: cd D:\\Antigravity\\pv_simulation_tool && .\\start_backend.bat"
        )


# ============================================================
# Einstiegspunkt
# ============================================================
if __name__ == "__main__":
    logger.info("PV Simulation Agent MCP Server wird gestartet...")
    logger.info(f"Backend-URL: {os.getenv('PV_SIM_BACKEND_URL', 'http://localhost:8000')}")
    mcp.run()
