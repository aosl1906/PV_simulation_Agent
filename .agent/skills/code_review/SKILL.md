---
name: code_review
description: Checkliste für Code-Reviews (Qualität, Sicherheit, Docs, Tests)
---

# Skill: Code Review

## Wann ist dieser Skill relevant?

- Nach Fertigstellung eines Features, bevor der PR gemergt wird.
- Wenn ein anderer Agent oder der User Code-Review anfordert.
- Als Selbst-Review (Antigravity prüft eigenen Code vor dem Commit).

---

## Code-Review Checkliste

### 1. Korrektheit & Logik
- [ ] Erfüllt der Code die Original-Anforderung vollständig?
- [ ] Werden Edge-Cases korrekt behandelt? (null, leer, negativ, sehr groß)
- [ ] Gibt es mögliche Race Conditions (besonders bei async Code)?
- [ ] Sind Fehler/Exceptions sinnvoll abgefangen?

### 2. Code-Qualität
- [ ] Sind Variablen- und Funktionsnamen selbsterklärend?
- [ ] Sind die Funktionen und Komponenten klein und fokussiert? (Single Responsibility)
- [ ] Gibt es duplizierte Logik, die extrahiert werden sollte? (DRY-Prinzip)
- [ ] Ist die Dateilänge noch akzeptabel? (< 150 Zeilen bei Komponenten empfohlen)
- [ ] Kommentare: Erklärt der Code sein „Warum", nicht nur sein „Was"?

### 3. Sicherheit
- [ ] Keine API-Keys, Passwörter oder Secrets im Code?
- [ ] Externe Eingaben werden validiert (API-Params, Formulardaten)?
- [ ] Keine SQL-Injection-Risiken (bei direkten Datenbankzugriffen)?

### 4. Tests
- [ ] Ist neue Logik durch Tests abgedeckt?
- [ ] Werden Tests in den korrekten Ordnern abgelegt? (laut `gemini.md`)
- [ ] Sind die Tests atomisch und unabhängig voneinander?

### 5. Dokumentation
- [ ] Sind neue oder geänderte öffentliche Funktionen/Methoden dokumentiert?
- [ ] Ist `CHANGELOG.md` aktualisiert?
- [ ] Ist `docs/architecture.md` noch aktuell (bei Architektur-Änderungen)?

### 6. Git-Hygiene
- [ ] Ist der Commit-Message-Stil korrekt? (Conventional Commits)
- [ ] Ist der Branch sauber? (kein unbezogener Code im PR)
- [ ] Keine temporären Debug-Statements (`console.log`, `print`) im Code?
- [ ] Keine unbeabsichtigten Dateien im Commit (`.env`, `*.log`)?

---

## Bewertung

| Ergebnis | Aktion |
|---|---|
| Alle Checkboxen grün | PR kann gemergt werden. |
| Leichte Mängel (Namensgebung, fehlende Kommentare) | In separatem Cleanup-Commit beheben. |
| Kritische Mängel (Security, falsche Logik, rote Tests) | Code zurückziehen, beheben, erneut reviewen. |

---

> **Regel:** Kein Merge mit bekannten kritischen Mängeln. Lieber einen Tag länger warten als technische Schulden einzuführen.
