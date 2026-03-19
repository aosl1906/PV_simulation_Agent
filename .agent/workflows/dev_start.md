---
description: Entwicklungsumgebung starten (MCP Server + PV Simulation Backend)
---

# /dev_start

---

## Voraussetzung: PV Simulation Backend starten

> ⚠️ Das PV Sim Backend muss ZUERST gestartet werden, da der MCP Server es als Dependency benötigt.

// turbo
1. PV Simulation Backend starten (separates Terminal):
```powershell
cd D:\Antigravity\pv_simulation_tool
.\start_backend.bat
```

---

## MCP Server starten

// turbo
2. MCP Server im Dev-Modus starten:
```powershell
cd D:\Antigravity\PV_simulation_Agent
python src/mcp_server.py
```

---

## Backend-Erreichbarkeit prüfen

// turbo
3. Prüfen ob PV Backend antwortet:
```powershell
python -c "import httpx; r = httpx.get('http://localhost:8000/'); print('OK' if r.status_code == 200 else 'FEHLER')"
```

---

**URLs nach dem Start:**
- PV Sim Backend: http://127.0.0.1:8000
- PV Sim API-Docs: http://127.0.0.1:8000/docs
- MCP Server: stdio-basiert (kein Port, wird von MCP Client verbunden)
