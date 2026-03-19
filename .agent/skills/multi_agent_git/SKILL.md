---
name: multi_agent_git
description: Git-Workflow für den parallelen Betrieb mehrerer AI-Agenten am gleichen Repository
---

# Skill: Multi-Agent Git Workflow

## Wann ist dieser Skill relevant?

Wenn mehrere Agenten (oder ein Agent in mehreren Sessions) parallel am gleichen Repository arbeiten, besteht das Risiko von Merge-Konflikten und inkonsistenten Zuständen. Dieser Skill beschreibt den verbindlichen Workflow.

---

## 1. Vor jeder Git-Operation: Status prüfen

Bevor irgendetwas committed oder gepusht wird:

```bash
git status             # Unverfolgte Dateien erkennen
git pull               # Neuesten Stand holen
git log --oneline -5   # Letzte 5 Commits sehen
```

> **Regel:** Niemals auf veralteter Basis arbeiten. Immer zuerst pullen.

---

## 2. Branch erstellen (Task-based Branching)

Jeder Agenten-Task bekommt seinen eigenen Branch:

```bash
git checkout -b feature/[kurze-feature-beschreibung]
# oder
git checkout -b bugfix/[kurze-bug-beschreibung]
# oder
git checkout -b docs/[was-dokumentiert-wird]
```

**Niemals direkt auf `main` committen!**

**Branch-Namenskonventionen:**
| Typ | Muster | Beispiel |
|---|---|---|
| Neues Feature | `feature/name` | `feature/user-authentication` |
| Bugfix | `bugfix/name` | `bugfix/login-crash` |
| Dokumentation | `docs/name` | `docs/api-reference-update` |
| Refactoring | `refactor/name` | `refactor/database-layer` |
| Tests | `test/name` | `test/add-integration-tests` |

---

## 3. Atomic Commits (Conventional Commits)

Commits sollten klein und atomar sein. Format: `<type>: <kurze Beschreibung>`

| Typ | Wann | Beispiel |
|---|---|---|
| `feat:` | Neues Feature | `feat: add password reset flow` |
| `fix:` | Bugfix | `fix: correct token expiry calculation` |
| `docs:` | Nur Dokumentation | `docs: update API reference for v2` |
| `refactor:` | Kein neues Feature, kein Bug | `refactor: extract auth logic into module` |
| `test:` | Tests hinzugefügt/geändert | `test: add integration tests for login` |
| `chore:` | Build, Abhängigkeiten, Config | `chore: update dependencies` |

**Pflicht vor jedem Commit:**
1. `/check_syntax` ausführen – Zero Syntax Errors on Handover.
2. `/run_tests` ausführen – Alle Tests müssen grün sein.
3. `git status` prüfen – Keine unbekannten Dateien committen.

---

## 4. Pull Request erstellen (via MCP)

Für GitHub-Repositories: Verwende den `mcp_github-mcp-server_create_pull_request` Tool, NICHT `run_command`.

```
Owner: [GitHub-Username oder Org]
Repo:  [Repository-Name]
Title: feat: [Feature-Beschreibung]
Head:  [Branch-Name]
Base:  main
Body:  [Kurze Beschreibung der Änderungen, was getestet wurde]
```

---

## 5. Konfliktbehandlung

**Bei Merge-Konflikten:**
1. **Sofort stoppen** — nicht blind auflösen.
2. **User informieren** — genau beschreiben, welche Dateien betroffen sind.
3. **Niemals `git push --force`!**
4. Konflikt gemeinsam mit User besprechen und lösen.

---

## 6. State-Tracking zwischen Sessions

Damit der nächste Agent (oder die nächste Session) weiss, wo wir stehen:
- `task.md` und `walkthrough.md` (Antigravity-Artefakte) immer aktuell halten.
- `CHANGELOG.md` direkt nach Abschluss eines Features aktualisieren.
- `ROADMAP.md` nach erledigten Features aktualisieren.
