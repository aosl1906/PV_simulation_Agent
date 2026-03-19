# PV Simulation Agent

> MCP Server, der das [PV Simulation Tool](../pv_simulation_tool/) als Tool-Set für KI-Agenten exponiert. Steuere PV-Simulationen per Klartext über Antigravity, Claude Desktop oder andere MCP-kompatible Clients.

---

## Voraussetzungen

- **Python** 3.10+: https://www.python.org/downloads/ (bei Installation: "Add Python to PATH" aktivieren!)
- **PV Simulation Tool**: Das Backend unter `D:\Antigravity\pv_simulation_tool` muss installiert und startbar sein.

---

## Installation & Start

1. **Repository klonen oder entpacken:**
   ```bash
   git clone <URL> PV_simulation_Agent
   cd PV_simulation_Agent
   ```

2. **Python-Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Umgebungsvariablen konfigurieren:**
   ```bash
   cp .env.example .env
   # .env mit eigenen Werten befüllen (siehe .agent/env_reference.md)
   ```

4. **PV Simulation Backend starten** (separates Terminal):
   ```bash
   cd D:\Antigravity\pv_simulation_tool
   .\start_backend.bat
   ```

5. **MCP Server starten:**
   ```bash
   python src/mcp_server.py
   ```

---

## MCP Client Konfiguration

### Antigravity / VS Code

In deiner MCP-Konfiguration (`settings.json` oder `.gemini/settings.json`) hinzufügen:

```json
{
  "mcpServers": {
    "pv-simulation": {
      "command": "python",
      "args": ["D:/Antigravity/PV_simulation_Agent/src/mcp_server.py"],
      "env": {
        "PV_SIM_BACKEND_URL": "http://localhost:8000"
      }
    }
  }
}
```

---

## Projektstruktur

```
PV_simulation_Agent/
├── .agent/       ← Agent-Konfiguration (Workflows, Skills)
├── docs/         ← Technische Dokumentation
├── schemas/      ← JSON-Schemas (SimulationRequest)
├── src/          ← Quellcode (MCP Server, Tool-Handler)
├── tests/        ← Tests (Unit, Integration)
├── gemini.md     ← Kollaborations-Richtlinien für Antigravity
├── README.md     ← Diese Datei
├── CHANGELOG.md  ← Versionshistorie
└── ROADMAP.md    ← Feature-Backlog
```

---

## 🤖 Antigravity Befehle (Slash-Commands)

| Befehl | Aktion |
|---|---|
| `/dev_start` | Startet MCP Server + PV Backend. |
| `/check_syntax` | Führt Lint- und Syntax-Checks aus. |
| `/run_tests` | Führt die automatisierten Tests aus. |

---

## Dokumentation

| Dokument | Inhalt |
|---|---|
| [`gemini.md`](./gemini.md) | Kollaborations-Richtlinien & Coding-Standards |
| [`docs/architecture.md`](./docs/architecture.md) | Systemarchitektur |
| [`ROADMAP.md`](./ROADMAP.md) | Geplante Features & Backlog |
| [`CHANGELOG.md`](./CHANGELOG.md) | Versionshistorie |

---

## Fehlerbehebung

- **"Connection refused" / Backend nicht erreichbar**: Das PV Simulation Backend muss zuerst gestartet werden (`start_backend.bat`). Prüfe ob Port 8000 antwortet.
- **"pip nicht gefunden"**: Verwende `python -m pip install -r requirements.txt` statt `pip install`.

---

*Erstellt mit dem [Antigravity Projekt-Template](https://github.com/aosl1/TEMPLATE).*
