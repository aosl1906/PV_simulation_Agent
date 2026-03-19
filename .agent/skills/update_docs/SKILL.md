---
name: update_docs
description: Proaktive Dokumentationspflege nach Feature-Änderungen oder Bugfixes
---

# Skill: Dokumentation aktualisieren

## Wann ist dieser Skill relevant?

Nach **jedem** Feature-Update, Bugfix oder Refactoring-Schritt.  
„Code is not done until Docs are done." — This is non-negotiable.

---

## Pflicht-Checkliste nach jeder Änderung

### 1. README.md
- [ ] Ist die Projekt-Beschreibung noch aktuell?
- [ ] Sind die Voraussetzungen (Versionen, Dependencies) korrekt?
- [ ] Stimmt die Schnellstart-Anleitung noch?
- [ ] Fehlt ein neues Feature in der Feature-Liste?

### 2. docs/architecture.md
- [ ] Hat sich die Systemarchitektur geändert? (neue Module, neue Services, neue Schichten)
- [ ] Sind neue Abhängigkeiten oder Integrationen hinzugekommen?
- [ ] Ist das Verzeichnis-Baum-Diagramm noch aktuell?

### 3. docs/API_REFERENCE.md (falls vorhanden)
- [ ] Neue Endpunkte hinzugefügt → dokumentieren.
- [ ] Bestehende Endpunkte geändert → aktualisieren.
- [ ] Endpunkte gelöscht → aus der Referenz entfernen.

### 4. CHANGELOG.md
- [ ] Die Änderung unter `[Unreleased]` eintragen.
- [ ] Format: `feat:`, `fix:`, oder `refactor:` + kurze Beschreibung.
- [ ] Bei einem Release: `[Unreleased]` → `[X.Y.Z] - YYYY-MM-DD` umbenennen.

### 5. ROADMAP.md
- [ ] Erledigte Features von „Priorisiert" oder „Backlog" nach „Erledigt" verschieben.
- [ ] Neue Ideen, die im Gespräch entstanden sind, im Backlog festhalten.

### 6. Projektspezifische Docs
<!-- SETUP: Zusätzliche Docs-Dateien nach Projekttyp eintragen. -->
- [ ] _[z.B. docs/TESTING.md – wenn Testabdeckung geändert wurde]_
- [ ] _[z.B. USER_MANUAL.md – wenn UI oder Workflows geändert wurden]_

---

## Prozess

1. Nach Abschluss des Codes: Diese Checkliste durchgehen.
2. Relevante Dokumente öffnen und anpassen.
3. Dann erst `git add` und Commit.

**Faustregel:** Wenn Du mehr als 30 Minuten an einer Änderung gearbeitet hast, lohnt sich mit Sicherheit eine Docs-Aktualisierung.

---

## Anti-Patterns (vermeiden!)

- ❌ CHANGELOG.md vergessen, dann nachträglich eintragen müssen.
- ❌ architecture.md veralten lassen — neue Entwickler/Agenten sind dann verwirrt.
- ❌ README.md mit falschen Start-Anweisungen — frustriert neue Projektmitglieder.
