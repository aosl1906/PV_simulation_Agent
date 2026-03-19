---
description: Syntax-Check für Backend und/oder Frontend durchführen
---

# /check_syntax

> **Pre-Test Check:** Bevor der User zum Testen aufgefordert wird, diesen Workflow ausführen.

---

## Python (Backend)

<!-- SETUP: Nur wenn Backend in Python. Sonst Abschnitt löschen. -->

// turbo
1. Ruff Lint-Check:
```powershell
# cd backend && python -m ruff check .
```

// turbo
2. Alternativ: pyflakes
```powershell
# cd backend && python -m pyflakes .
```

---

## JavaScript / TypeScript (Frontend)

<!-- SETUP: Nur wenn Frontend in JS/TS. Sonst Abschnitt löschen. -->

// turbo
3. ESLint:
```powershell
# cd frontend && npm run lint
```

// turbo
4. TypeScript Type-Check (nur bei TypeScript):
```powershell
# cd frontend && npm run type-check
# oder: npx tsc --noEmit
```

---

## Ergebnis

- **Keine Fehler** → Syntax korrekt. Weiter mit Tests oder Commit.
- **Fehler gefunden** → Zuerst beheben! Regel: „Zero Syntax Errors on Handover."

---

> **Antigravity-Regel:** Niemals Code mit bekannten Syntaxfehlern committen.
