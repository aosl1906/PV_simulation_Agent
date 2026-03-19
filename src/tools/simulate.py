"""
Module: src/tools/simulate.py

Beschreibung:
    MCP Tool-Handler für PV-Simulationen.
    Baut ein SimulationRequest-JSON aus den übergebenen Parametern
    und ruft POST /simulate auf dem PV Simulation Backend auf.

Wichtig:
    - Das Backend rechnet pvlib (PV-Ertrag) intern — wir senden nur
      tilt, azimuth, peak_power_kw.
    - Alle optionalen Parameter haben sinnvolle Defaults im Backend.
    - Der Agent muss nur die essentiellen Parameter liefern.
"""
import logging
from typing import Any

from src.utils.http_client import post_json, check_backend_health

logger = logging.getLogger("mcp.tools.simulate")


def build_simulation_request(
    latitude: float,
    longitude: float,
    arrays: list[dict],
    battery_capacity_kwh: float = 0.0,
    battery_max_charge_kw: float = 5.0,
    battery_max_discharge_kw: float = 5.0,
    annual_consumption_kwh: float = 4500.0,
    consumption_type: str = "family",
    heat_pump_enabled: bool = False,
    heat_pump_annual_demand_kwh: float = 10000.0,
    heat_pump_flow_temp: float = 35.0,
    wallbox_enabled: bool = False,
    wallbox_battery_kwh: float = 50.0,
    wallbox_daily_km: float = 40.0,
    wallbox_charge_power_kw: float = 11.0,
    hems_enabled: bool = False,
    electricity_price_eur: float = 0.30,
    feed_in_tariff_eur: float = 0.08,
) -> dict:
    """
    Baut ein vollständiges SimulationRequest-Dict aus den übergebenen Parametern.
    Verwendet Defaults für alles, was nicht explizit angegeben wird.
    """
    # PV Arrays aufbereiten
    pv_arrays = []
    for arr in arrays:
        pv_arrays.append({
            "name": arr.get("name", "PV Array"),
            "tilt": arr.get("tilt", 30.0),
            "azimuth": arr.get("azimuth", 180.0),
            "peak_power_kw": arr.get("peak_power_kw", 5.0),
        })

    request = {
        "latitude": latitude,
        "longitude": longitude,
        "arrays": pv_arrays,
        "consumption_params": {
            "annualKwh": annual_consumption_kwh,
            "type": consumption_type,
        },
        "economics_params": {
            "electricityPriceEurPerKwh": electricity_price_eur,
            "feedInTariffEurPerKwh": feed_in_tariff_eur,
        },
    }

    # Batterie (nur wenn Kapazität > 0)
    if battery_capacity_kwh > 0:
        request["battery_params"] = {
            "capacity_kwh": battery_capacity_kwh,
            "max_charge_kw": battery_max_charge_kw,
            "max_discharge_kw": battery_max_discharge_kw,
        }

    # Wärmepumpe
    if heat_pump_enabled:
        request["heat_pump_params"] = {
            "enabled": True,
            "annualHeatDemandKwh": heat_pump_annual_demand_kwh,
            "flowTempMinus10": heat_pump_flow_temp,
        }

    # E-Auto / Wallbox
    if wallbox_enabled:
        request["wallbox_params"] = {
            "enabled": True,
            "battery_capacity_kwh": wallbox_battery_kwh,
            "max_charge_power_kw": wallbox_charge_power_kw,
            "consumption_kwh_100km": 18.0,
            "daily_distance_km": wallbox_daily_km,
        }

    # HEMS
    if hems_enabled:
        request["hems_params"] = {
            "enabled": True,
            "pv_surplus_charging": True,
            "smart_forecast_charging": True,
        }

    return request


def format_summary(results: dict) -> str:
    """
    Formatiert die Simulationsergebnisse als lesbaren Text.
    Extrahiert die wichtigsten KPIs aus dem Summary.
    """
    summary = results.get("summary", {})
    if not summary:
        return "Keine Ergebnisse verfügbar."

    total_yield = summary.get("total_yield_kwh", 0)
    total_consumption = summary.get("total_consumption_kwh", 0)
    self_consumption = summary.get("self_consumption_kwh", 0)
    grid_export = summary.get("grid_export_kwh", 0)
    grid_import = summary.get("grid_import_kwh", 0)
    autarky = summary.get("autarky_percent", 0)
    self_cons_pct = summary.get("self_consumption_percent", 0)

    lines = [
        "## Simulationsergebnisse",
        "",
        "| Kennwert | Wert |",
        "|---|---|",
        f"| ☀️ PV-Ertrag (Jahres) | {total_yield:,.0f} kWh |",
        f"| ⚡ Gesamtverbrauch | {total_consumption:,.0f} kWh |",
        f"| 🏠 Eigenverbrauch | {self_consumption:,.0f} kWh ({self_cons_pct:.1f}%) |",
        f"| 🔌 Netzbezug | {grid_import:,.0f} kWh |",
        f"| 📤 Netzeinspeisung | {grid_export:,.0f} kWh |",
        f"| 🎯 Autarkie | {autarky:.1f}% |",
    ]

    # Batterie-Info wenn vorhanden
    batt_cycles = summary.get("battery_cycles", 0)
    if batt_cycles > 0:
        lines.append(f"| 🔋 Batterie-Vollzyklen | {batt_cycles:.0f} |")

    # Wirtschaftlichkeit wenn vorhanden
    savings = summary.get("annual_savings_eur", 0)
    if savings > 0:
        lines.append(f"| 💰 Jährliche Ersparnis | {savings:,.0f} € |")

    return "\n".join(lines)


async def run_simulation(params: dict) -> dict[str, Any]:
    """
    Führt eine Simulation über das PV Backend aus.

    Returns:
        Dict mit 'summary_text' (formatiert) und 'raw_summary' (dict)
    """
    # Prüfe Backend-Erreichbarkeit
    healthy = await check_backend_health()
    if not healthy:
        return {
            "error": "PV Simulation Backend nicht erreichbar. "
                     "Bitte sicherstellen, dass es auf "
                     "PV_SIM_BACKEND_URL läuft (default: http://localhost:8000)."
        }

    logger.info("Starte PV-Simulation...")
    try:
        results = await post_json("/simulate", params)
        summary_text = format_summary(results)

        return {
            "summary_text": summary_text,
            "raw_summary": results.get("summary", {}),
        }
    except Exception as e:
        logger.error(f"Simulation fehlgeschlagen: {e}", exc_info=True)
        return {"error": f"Simulation fehlgeschlagen: {str(e)}"}
