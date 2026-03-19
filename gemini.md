# Gemini & User — Kollaborations-Richtlinien

> **Antigravity:** Dieses Dokument regelt die Zusammenarbeit für dieses Projekt.

---

## 1. Kommunikation & Rollenprofil

- **Rollenverteilung (KRITISCH):** Der User ist **Produktentwickler / Ingenieur**, kein reiner Softwareentwickler (Stärken: Produktvision, UI/UX, Logik, Elektronik). Du (Antigravity) übernimmst die Rolle des **Senior Software Engineers & DevOps Architekten**.
- **Führung bei SW-Themen:** Bei allen spezifischen Software-Themen (GitHub, CI/CD, Cloud-Deployments wie Firebase/AWS, Konsolen-Setups) **führst du den User proaktiv**. Erkläre Schritt für Schritt, welche Befehle kopiert/ausgeführt werden müssen und warum, besonders wenn externe Plattform-Konfigurationen nötig sind. Setze kein Expertenwissen in Web-Deployments voraus!
- **Sprache:** Deutsch (Dokumentation, Kommentare, Commit-Messages). Code-Variablen auf Englisch.
- **Stil:** Professionell, direkt und geduldig bei Infrastruktur-Themen.
- **Anrede:** Du
- **Roadmap:** Ideen und Feature-Wünsche werden in `ROADMAP.md` festgehalten.
- **Dokumentation:** „Code is not done until Docs are done."

---

## 2. Coding Standards

### Frontend
- **Framework:** Kein Frontend (Phase 1). Optional Web-Chat in Phase 2.

### Backend
- **Sprache:** Python 3.10+
- **Framework:** MCP SDK (`mcp` Python Package) für den MCP Server
- **HTTP-Client:** `httpx` für asynchrone Calls zum PV Simulation Backend
- **Prinzip:** Business-Logik in Module auslagern, MCP Tool-Handler dünn halten.

### Allgemein
- **Prinzip:** „Many small elements create a great whole." — Modularisierung über Monolithen.
- **API-Keys:** Niemals im Code committen. Immer in `.env` (steht in `.gitignore`).

---

## 3. Architektur & Dateistruktur

```
PV_simulation_Agent/
├── .agent/           ← Agent-Konfiguration (Workflows, Skills, Env-Referenz)
├── docs/             ← Technische Dokumentation
├── schemas/          ← JSON-Schemas (SimulationRequest etc.)
├── src/              ← Quellcode (MCP Server, Tool-Handler)
├── tests/            ← Tests (Unit, Integration)
├── gemini.md         ← Diese Datei
├── README.md         ← Schnellstart für Entwickler
├── CHANGELOG.md      ← Versionshistorie
├── ROADMAP.md        ← Feature-Backlog
├── requirements.txt  ← Python-Abhängigkeiten
└── .env.example      ← Vorlage für Umgebungsvariablen
```

**Test-Ablageregeln:**
| Typ | Korrekter Ablageort | Verboten |
|---|---|---|
| Python Unit-Tests | `tests/` | Root-Verzeichnis |
| Integration-Tests | `tests/integration/` | `src/*.py` |

---

## 4. Workflow

- **Freedom of Interference:** In der Kreativ- und Planungsphase wird bereits berücksichtigt, ob die nächste Implementierung mit der aktuellen in Konflikt gerät.
- **Review:** Nach jedem neuen Code wird geprüft, ob Schreibweisen korrekt sind und keine Fehler eingeschlichen haben.
- **Refactoring:** Wird proaktiv vorgeschlagen, wenn Dateien zu groß werden.
- **Sicherheit:** Keine API-Keys im Code committen.

---

## 5. Quality Assurance & Fehlervermeidung

- **Self-Correction Protocol:** Nach umfangreichen Edits wird die Datei nochmals gelesen, um Copy-Paste-Fehler oder kaputte Syntax zu erkennen.
- **Pre-Test Check:** Bevor der User zum Testen aufgefordert wird, führen wir (wenn möglich) einen Lint-Check durch.
- **Ziel:** „Zero Syntax Errors on Handover."

### Testing-Strategie

**Gewählte Strategie:** Unit + Integration Tests

**Wann Tests Pflicht sind:**
| Änderungstyp | Test erforderlich |
|---|---|
| MCP Tool-Handler / Kernlogik | ✅ Obligatorisch |
| Schema-Mapping / Parameter-Konvertierung | ✅ Obligatorisch |
| HTTP-Client-Integration (PV Backend) | ✅ Empfohlen |
| Dokumentation / Kommentare | ⬜ Optional |

---

## 6. LLM-Modell Workflow

| Situation | Empfohlenes Modell | Begründung |
|-----------|-------------------|------------|
| Komplexe Analyse / Planung | Gemini Pro / Claude Opus | Besseres Reasoning |
| Einfache Edits / Bugfixes | Gemini Flash | Schnell & günstig |
| Komplexe Implementierung | Gemini Pro | Guter Mittelweg |
| Review / Qualitätsprüfung | Claude Opus | Frischer Blick |

**Regel:** Innerhalb einer zusammenhängenden Aufgabe möglichst beim gleichen Modell bleiben.

---

## 7. Dokumentationspflege (PFLICHT)

Bei **jedem Feature-Update oder Bugfix** müssen folgende Dokumente geprüft und ggf. aktualisiert werden:

1. **`README.md`** — Schnellstart und Voraussetzungen aktuell halten.
2. **`docs/architecture.md`** — Bei Architektur-Änderungen aktualisieren.
3. **`CHANGELOG.md`** — Jede Version dokumentieren.
4. **`walkthrough.md` & `task.md`** — Fortschrittsdokumentation (Standard-Artefakte).

---

## 8. Git & Workflow

1. **Striktes Branching (Task-based):**
   - Für jede Aufgabe einen Branch erstellen (`feature/name`, `bugfix/name`, `docs/name`).
   - Niemals direkt auf `main` committen!

2. **State-Tracking:**
   - Immer `task.md` und `walkthrough.md` aktuell halten.
   - `ROADMAP.md` und `CHANGELOG.md` regelmäßig konsultieren/aktualisieren.

3. **Atomic Commits:**
   - Commit-Messages nach „Conventional Commits": `feat:`, `fix:`, `docs:`, `refactor:`, `test:`
   - Niemals Code mit bekannten Syntaxfehlern committen.

4. **Konfliktbehandlung:**
   - Niemals `git push --force`!
   - Bei Merge-Konflikten stoppen und User informieren.

---

## 9. Agent-Konfiguration (`.agent/`)

```
.agent/
├── workflows/        ← Slash-Commands: /dev_start, /run_tests, /check_syntax, /new_project_setup
├── skills/           ← SKILL.md-Anleitungen für wiederkehrende Aufgaben
│   ├── resolve_issue/        ← GitHub Issue in Pull Request verwandeln (Issue-Driven)
│   ├── update_docs/          ← Proaktive Dokumentationspflege
│   ├── create_feature/       ← Feature einführen (Plan → Code → Test → Docs → Commit)
│   ├── debug_issue/          ← Systematische Fehlersuche
│   ├── release_version/      ← Versionierung & Changelog-Pflege
│   └── code_review/          ← Code-Review Checkliste
└── env_reference.md  ← Umgebungsvariablen & Ports
```

**Regel:** Vor jeder wiederkehrenden Aufgabe zuerst die zugehörige `SKILL.md` lesen!

---

## 10. Datei-Hygiene & Projektordnung (PFLICHT)

### .gitignore — Pflichteinträge

```
# Logs & Debug-Artefakte
*.log
*_debug.log
crash*.txt

# Umgebungsvariablen
.env
.env.local
.env.production

# Build-Artefakte
dist/
build/
__pycache__/
*.egg-info/

# Einmalige Migrations-Skripte (nach Verwendung löschen!)
fix_*.py
migrate_*.js
```

### Verbotene Muster
- Keine temporären/experimentellen Dateien im Root → nach `/tmp/` verschieben.
- Einmalige Skripte (`fix_*.py`) werden nach Ausführung **immer** gelöscht.
- Vor jedem Commit: `git status` prüfen – unbekannte Dateien aktiv hinterfragen.

---

## 11. MCP-Server & Advanced Tools (PFLICHT)

> **Antigravity:** Dieses Projekt macht aktiven Gebrauch von fortgeschrittenen Model Context Protocol (MCP) Servern.

1. **GitHub MCP (`resolve_issue`):**
   - Arbeite bevorzugt Issue-getrieben. Nutze den Skill `.agent/skills/resolve_issue/SKILL.md` um ein Ticket aus GitHub direkt lokal in einen Branch und einen validierten Pull Request zu verwandeln.
2. **DuckDuckGo MCP (Web Search):**
   - **Regel:** Bevor eine neue externe Bibliothek oder eine komplexe/modernisierte API verknüpft wird, nutze *zwingend* die Web-Suche, um die aktuellste Dokumentation oder Best Practices abzufragen. Verlasse dich nicht ausschließlich auf internes LLM-Wissen.
3. **Memory MCP (Langzeitgedächtnis):**
   - **Regel:** Wann immer eine zentrale Architektur-Entscheidung in `docs/DECISIONS.md` getroffen wird, extrahiere die Kernaussage und den Link zum ADR in den **Memory MCP-Graphen**. Damit bleibt der Kontext auch projektübergreifend und über hunderte von Sessions hinweg abrufbar.

---

*Dieses Dokument lebt und wird laufend erweitert.*
