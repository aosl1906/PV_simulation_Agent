---
name: resolve_issue
description: Integrierter Workflow um ein GitHub Issue komplett und systematisch in einen fertigen Pull Request zu verwandeln
---

# Skill: Issue lösen (Issue-Driven Development)

## Wann ist dieser Skill relevant?

Wenn du beauftragt wirst, in GitHub erfasste Aufgaben oder Bugs systematisch zu bearbeiten. Dieser Skill verbindet die externe Ticket-Verfolgung mit der lokalen Entwicklung.

---

## 1. Issue analysieren (Info-Gathering)

Verwende den **GitHub MCP Server** (z.B. in der Antigravity-Konsole), um das Issue vorab auszulesen:
- `mcp_github-mcp-server_search_issues` zum Finden oder
- `mcp_github-mcp-server_issue_read` wenn die ID bekannt ist.

Analysiere:
- Was ist die exakte Anforderung? Gibt es technische Constraints in den Kommentaren?

---

## 2. Branch anlegen

Erstelle einen frischen Branch für die Bearbeitung, der die Issue-ID referenziert.

```bash
git checkout -b feature/[issue-id]-[kurze-beschreibung]
# oder
git checkout -b bugfix/[issue-id]-[kurze-beschreibung]
```
*(z.B. `git checkout -b feature/42-auth-google`)*

> **Regel:** Direkte Code-Änderungen an Issues auf dem Hauptbranch sind streng verboten.

---

## 3. Planen & Abstimmen (PLANNING)

1. Mache dir einen Umsetzungsplan in `task.md`.
2. Wenn das Issue unklar ist: Nutze das Tool `mcp_github-mcp-server_add_issue_comment`, um direkt im Ticket nachzufragen, oder sprich den User an.
3. Erst weiterarbeiten, wenn Klarheit herrscht.

---

## 4. Implementieren & Testen (EXECUTION)

Jetzt nach dem bewährten Skill `create_feature` programmieren:
- Kleinere Module schreiben
- `/check_syntax` regelmäßig laufen lassen
- Tests nach `/run_tests` sichern

---

## 5. Dokumentation pflegen

Aktualisiere die Dokumentation nach Skill `update_docs`.
**Wichtig:** Vermerke im `CHANGELOG.md` die referenzierte Ticketnummer:
`feat: Adds Google Authentication flow (#42)`

---

## 6. PR erstellen (Abschluss)

Gib die erledigte Arbeit zur Prüfung (Code-Review) frei. Nutze dazu das Tool `mcp_github-mcp-server_create_pull_request`.

**PR-Format:**
- Nutze das Auto-Close Keyword im PR Body: `Fixes #[ID]` oder `Closes #[ID]`.
- Schreibe kurz auf, **was** gemacht wurde und **welche Tests** es validieren.
