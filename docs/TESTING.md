# Testing-Strategie

> **Projekt:** _[Projektname]_

<!-- SETUP: Testing-Strategie aus SETUP_GUIDE.md Phase 4 hier eintragen. -->

---

## Gewählte Strategie

<!-- SETUP: Eine Option wählen und die anderen entfernen. -->

| Option | Beschreibung | Geeignet für |
|---|---|---|
| **A – Minimal** | Manuelle Tests, strukturierte Tests nur bei Bedarf | Prototypen, kleine Tools |
| **B – Standard** (empfohlen) | Unit-Tests + Integration-Tests | Die meisten Projekte |
| **C – Vollständig** | Zusätzlich SIL / E2E-Tests | Kritische Systeme, Safety-relevant |

**Gewählt:** _[Option A / B / C]_

---

## Test-Ablageregeln

<!-- SETUP: Ablageregeln je nach Tech-Stack befüllen. -->

| Test-Typ | Korrekter Ort | Verboten |
|---|---|---|
| _[z.B. Python Unit-Tests]_ | _[z.B. backend/tests/unit/]_ | _[z.B. backend/*.py]_ |
| _[z.B. Python Integration-Tests]_ | _[z.B. backend/tests/integration/]_ | — |
| _[z.B. JS/React Tests]_ | _[z.B. frontend/src/__tests__/]_ | _[z.B. frontend/src/*.test.js im Root]_ |
| _[z.B. SIL-Tests]_ | _[z.B. backend/tests/sil/]_ | — |

---

## Wie Tests ausgeführt werden

```bash
# /run_tests Workflow ausführen
# oder manuell:

# [Konkreten Testbefehl eintragen]
# Beispiel Python: python -m pytest tests/ -v --tb=short
# Beispiel Node:   npm run test
```

---

## Wann Tests Pflicht sind

<!-- SETUP: Tabelle projektspezifisch befüllen. -->

| Änderungstyp | Test erforderlich |
|---|---|
| _[Kernlogik / Algorithmen]_ | ✅ Obligatorisch |
| _[API-Routes]_ | ✅ Empfohlen |
| _[Datenbank-Migrationen]_ | ✅ Empfohlen |
| _[Reine UI / Styling-Änderungen]_ | ⬜ Optional |
| _[Dokumentations-Änderungen]_ | ⬜ Nicht erforderlich |

---

## Test-Qualitätsregeln

1. **Atomisch:** Jeder Test prüft genau eine Sache.
2. **Unabhängig:** Tests dürfen keinen gemeinsamen State teilen.
3. **Deterministisch:** Kein Test darf von externen Services abhängen (Mocking verwenden).
4. **Aussagekräftig:** Test-Namen beschreiben was getestet wird: `test_login_fails_with_wrong_password`.

---

## SIL/E2E-Tests (nur Strategie C)

<!-- SETUP: Falls nicht verwendet: Abschnitt löschen. -->

_[Beschreibung des SIL/E2E-Test-Setups, Invarianten, kritische Szenarien]_

---

*Tests werden nach dem `create_feature` Skill (Schritt 5) erstellt.*
