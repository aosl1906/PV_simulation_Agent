---
name: create_feature
description: Schritt-für-Schritt-Anleitung zum Einführen eines neuen Features (Plan → Code → Test → Docs → Commit)
---

# Skill: Feature einführen

## Überblick

Jedes neue Feature folgt diesem strukturierten Prozess. Kein Schritt wird übersprungen.

```
Plan → Code → Syntax-Check → Tests → Docs → Commit → PR
```

---

## Schritt 1: Planen (PLANNING-Mode)

**Bevor die erste Zeile Code geschrieben wird:**

1. Anforderung vollständig verstehen. Falls unklar: User fragen.
2. `implementation_plan.md` (Artefakt) erstellen:
   - Was wird geändert? (Dateiliste)
   - Welche Abhängigkeiten sind betroffen?
   - Welche Tests werden benötigt?
   - Wie wird verifiziert, dass es funktioniert?
3. Plan mit dem User reviewen lassen, bevor gestartet wird.

**Checkliste Plan:**
- [ ] Änderungsumfang klar definiert
- [ ] Betroffene Dateien identifiziert
- [ ] Keine Konflikte mit anderen Features erkennbar (Freedom of Interference)
- [ ] Teststrategie festgelegt
- [ ] User hat Plan bestätigt

---

## Schritt 2: Branch erstellen

```bash
git checkout -b feature/[name-des-features]
```

Niemals auf `main` direkt entwickeln!

---

## Schritt 3: Implementieren (EXECUTION-Mode)

**Beim Coden:**
- Kleine, atomare Schritte. Nicht alles auf einmal.
- Komponenten-Prinzip: Dateien < 150 Zeilen wenn möglich.
- Business-Logik in separate Module auslagern.
- Keine API-Keys oder Secrets im Code.
- Nach jedem größeren Edit: Datei kurz gegenlesen (Self-Correction Protocol).

**Häufige Fallen:**
- Copy-Paste-Fehler in langen Funktionen.
- Kaputte Importe nach Umbenennung einer Datei.
- Vergessene Edge-Cases (leere Listen, null-Werte, Netzwerkfehler).

---

## Schritt 4: Syntax-Check

```bash
# /check_syntax ausführen (Workflow)
```

Keine Fehler? Weiter mit Tests.  
Fehler gefunden? Zuerst beheben.

---

## Schritt 5: Tests ausführen

```bash
# /run_tests ausführen (Workflow)
```

Alle Tests grün? Weiter.  
Tests rot? Root Cause analyse, beheben, erneut testen.

**Neue Tests schreiben (falls nötig):**
- Unit-Tests für neue Logik-Funktionen.
- Integration-Tests wenn Systemgrenzen überschritten werden (API, DB, …).
- Tests in den vorgesehenen Ordner ablegen (laut `gemini.md` Abschnitt Test-Ablageregeln).

---

## Schritt 6: Dokumentation aktualisieren

Skill `update_docs` lesen und die Checkliste durchgehen:
- README.md, architecture.md, API_REFERENCE.md, CHANGELOG.md, ROADMAP.md.

---

## Schritt 7: Commit & Pull Request

```bash
git add .
git commit -m "feat: [kurze, präzise Beschreibung]"
git push origin feature/[name-des-features]
```

PR erstellen via MCP (GitHub) oder User informieren.  
PR-Beschreibung enthält:
- Was wurde geändert?
- Wie wurde getestet?
- Screenshots / Demo (falls UI-Änderung)?

---

## Schritt 8: Walkthrough erstellen (VERIFICATION-Mode)

`walkthrough.md` Artefakt aktualisieren:
- Was wurde implementiert?
- Was wurde getestet?
- Validierungs-Ergebnisse.
