# Umgebungsvariablen-Referenz

> Die tatsächlichen Werte stehen in `.env` (nicht im Git!). Diese Datei dokumentiert nur die Struktur.

---

## MCP Server (`.env` im Projekt-Root)

| Variable | Typ | Beschreibung | Beispiel |
|---|---|---|---|
| `PV_SIM_BACKEND_URL` | String | URL des PV Simulation Backends | `"http://localhost:8000"` |

**Hinweise:**
- Nie committen! Steht in `.gitignore`
- Vorlage liegt in `.env.example`

---

## Ports (lokal)

| Service | Port | URL |
|---|---|---|
| PV Sim Backend (extern, muss separat gestartet werden) | 8000 | http://127.0.0.1:8000 |
| MCP Server | — | stdio-basiert (kein Port nötig) |

---

## Bekannte Eigenheiten

| Thema | Verhalten | Korrekte Verwendung |
|---|---|---|
| PV Backend muss separat laufen | MCP Server startet es NICHT automatisch | Erst `pv_simulation_tool` Backend starten, dann MCP Server |
| pip nicht im PATH | pip schlägt fehl | `python -m pip` verwenden |

---

*Letzte Aktualisierung: 2026-03-19*
