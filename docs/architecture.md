# Systemarchitektur

> **Stand:** 2026-03-19  
> **Projekt:** PV Simulation Agent

---

## 1. Systemüberblick

Der PV Simulation Agent ist ein **MCP Server** (Model Context Protocol), der das bestehende `pv_simulation_tool` Backend als Tool-Set für KI-Agenten exponiert. Der Agent selbst enthält kein LLM — er wird von MCP-fähigen Clients (Antigravity, Claude Desktop, etc.) gesteuert.

```
┌─────────────────┐     MCP Protocol      ┌──────────────────────┐
│  MCP Client      │ ◄──── stdio/SSE ────► │  PV Sim MCP Server   │
│  (Antigravity,   │                       │  (Python, mcp SDK)   │
│   Claude, etc.)  │                       │                      │
└─────────────────┘                        │  Tools:              │
                                           │  • simulate_project  │
                                           │  • get_schema        │
                                           │  • geocode_address   │
                                           │  • analyze_*         │
                                           └──────┬───────────────┘
                                                  │ HTTP (httpx)
                                                  ▼
                                           ┌──────────────────────┐
                                           │  PV Sim Backend      │
                                           │  (FastAPI, Port 8000)│
                                           │  (UNVERÄNDERT!)      │
                                           └──────────────────────┘
```

**Kern-Prinzip:** Der MCP Server ist ein reiner **Adapter/Wrapper**. Keine Simulation-Logik wird dupliziert.

---

## 2. Backend-Architektur (MCP Server)

### 2.1 Technologie-Stack

- **Sprache:** Python 3.10+
- **MCP SDK:** `mcp` (offizielles Anthropic/MCP Python SDK)
- **HTTP-Client:** `httpx` (async) für Kommunikation mit PV Sim Backend
- **Datenbank:** Keine
- **Deployment:** Lokal (Phase 1), optional Cloud (Phase 2)

### 2.2 Verzeichnisstruktur

```
PV_simulation_Agent/
├── src/
│   ├── mcp_server.py       ← MCP Server Hauptdatei (Tool-Registrierung)
│   ├── tools/              ← Einzelne Tool-Handler
│   │   ├── simulate.py     ← simulate_project Tool
│   │   ├── analyze.py      ← Sensitivity / Battery-Opt Tools
│   │   └── geocode.py      ← Adresse → lat/lon Konvertierung
│   └── utils/
│       ├── http_client.py  ← httpx Wrapper für PV Backend API
│       └── schema.py       ← Schema-Export und Validation
├── schemas/
│   └── simulation_schema.json  ← Exportiertes JSON-Schema
├── tests/
│   ├── test_tools.py       ← Unit-Tests für Tool-Handler
│   └── integration/
│       └── test_backend.py ← Integration-Tests (benötigt PV Backend)
├── requirements.txt
└── .env.example
```

### 2.3 Datenfluss

1. **User → MCP Client:** Klartext-Anfrage (z.B. "Simuliere 10 kWp in München")
2. **MCP Client → MCP Server:** Tool-Call `simulate_project` mit JSON-Parametern
3. **MCP Server → PV Backend:** HTTP POST `/simulate` mit `SimulationRequest`
4. **PV Backend → MCP Server:** JSON-Response mit Summary + Hourly-Daten
5. **MCP Server → MCP Client:** Gefilterte/zusammengefasste Ergebnisse
6. **MCP Client → User:** Natürlichsprachliche Zusammenfassung

### 2.4 Wichtige Konventionen

- **PV Backend muss laufen:** Der MCP Server setzt voraus, dass das PV Sim Backend auf `PV_SIM_BACKEND_URL` (default: `http://localhost:8000`) erreichbar ist.
- **pvlib intern:** Das Backend rechnet PV-Erträge selbst. Der Agent braucht nur `tilt`, `azimuth`, `peak_power_kw` — keine vorberechneten Ertragskurven.
- **Defaults:** Die Pydantic-Schemas im Backend haben sinnvolle Defaults für alle optionalen Parameter. Der Agent muss nur die essentiellen Parameter (Standort, PV-Konfiguration, Verbrauch) liefern.

---

## 3. Externe Integrationen

| Service | Zweck | Konfiguration |
|---|---|---|
| PV Simulation Backend | Physik-Simulation, PDF-Export | `PV_SIM_BACKEND_URL` in `.env` |
| Nominatim / OpenStreetMap | Geocoding (Adresse → lat/lon) | Frei verfügbar, kein API-Key |

---

## 4. MCP Tools (Überblick)

| Tool-Name | Backend-Endpunkt | Beschreibung |
|---|---|---|
| `get_simulation_schema` | — (lokal) | JSON-Schema für SimulationRequest |
| `simulate_project` | `POST /simulate` | PV-Simulation ausführen |
| `analyze_sensitivity` | `POST /api/analyze_sensitivity` | Sensitivitätsanalyse |
| `analyze_battery_optimization` | `POST /api/analyze_battery_opt` | Batterieoptimierung |
| `geocode_address` | Nominatim API | Adresse → Koordinaten |

---

## 5. Test-Architektur

Detailliert in [`docs/TESTING.md`](./TESTING.md).

---

*Dieses Dokument wird bei jeder Architektur-Änderung aktualisiert (Skill: `update_docs`).*
