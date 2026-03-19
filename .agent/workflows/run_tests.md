---
description: Alle Tests ausführen und Ergebnisse prüfen
---

# /run_tests

> **SETUP:** Mit den konkreten Test-Befehlen des Projekts befüllen.

---

## Backend-Tests

<!-- SETUP: Befehl eintragen. Beispiele hinterlassen. -->

// turbo
1. Backend-Tests ausführen:
```powershell
# Python/pytest Beispiel:
# cd backend && python -m pytest tests/ -v --tb=short

# Node/Vitest Beispiel:
# cd frontend && npm run test

# [Konkreten Befehl eintragen]
```

---

## Frontend-Tests (falls vorhanden)

// turbo
2. Frontend-Tests ausführen:
```powershell
# [z.B.: cd frontend && npm run test:unit]
```

---

## Ergebnisse interpretieren

- Alle Tests **PASSED** → Änderungen sind sicher. Commit möglich.
- Tests **FAILED** → Abbruch! Fehler analysieren, beheben, dann erneut testen.

---

## Wann muss `/run_tests` ausgeführt werden?

<!-- SETUP: Tabelle aus gemini.md (Abschnitt Testing-Strategie) übernehmen. -->

| Änderungstyp | Test erforderlich |
|---|---|
| _[Kernlogik / Algorithmen]_ | ✅ Obligatorisch |
| _[API-Routes]_ | ✅ Empfohlen |
| _[Reine UI-Änderungen]_ | ⬜ Optional |
