---
name: release_version
description: Versionierung und Changelog-Pflege nach Semantic Versioning
---

# Skill: Version releasen

## Semantic Versioning — Kurzreferenz

Format: `MAJOR.MINOR.PATCH` (z.B. `1.3.2`)

| Typ | Wann | Beispiel |
|---|---|---|
| PATCH | Bugfix ohne API-Änderung | `1.3.1 → 1.3.2` |
| MINOR | Neues Feature, rückwärtskompatibel | `1.3.2 → 1.4.0` |
| MAJOR | Breaking Change, inkompatible API-Änderung | `1.4.0 → 2.0.0` |

---

## Release-Prozess

### Schritt 1: CHANGELOG.md vorbereiten

1. `CHANGELOG.md` öffnen.
2. `[Unreleased]` Abschnitt in `[X.Y.Z] - YYYY-MM-DD` umbenennen.
3. Neuen leeren `[Unreleased]` Abschnitt darüber einfügen.
4. Alle Einträge unter die korrekten Kategorien gruppieren:
   - `Added` / `Changed` / `Fixed` / `Deprecated` / `Removed`

### Schritt 2: Version im Projekt aktualisieren

<!-- SETUP: Je nach Tech-Stack die relevante Datei eintragen. -->
- **Python:** `pyproject.toml` oder direkt in `__init__.py`
- **Node.js:** `package.json` → `"version": "X.Y.Z"`
- **Anderes:** _[Projektspezifisch eintragen]_

### Schritt 3: Alle Tests ausführen

```bash
# /run_tests ausführen
```

Kein Release mit roten Tests!

### Schritt 4: Release-Commit erstellen

```bash
git add CHANGELOG.md [andere geänderte Dateien]
git commit -m "chore: release v[X.Y.Z]"
git tag v[X.Y.Z]
git push origin main --tags
```

### Schritt 5: GitHub Release erstellen (optional)

Via MCP-Tool `mcp_github-mcp-server_create_release`:
- Tag: `vX.Y.Z`
- Title: `v[X.Y.Z] – [Kurzer Release-Titel]`
- Body: Relevante Einträge aus CHANGELOG.md kopieren.

---

## Changelog-Einträge — Qualitätsregeln

**Gute Einträge:**
- ✅ `Added: Benutzer können jetzt ihr Passwort zurücksetzen.`
- ✅ `Fixed: Absturz bei leerem Formular-Submit behoben.`

**Schlechte Einträge:**
- ❌ `Added: Code geändert.`
- ❌ `Fixed: Bug behoben.`
- ❌ `Updated: Stuff.`

**Regel:** Jeder Eintrag erklärt den User-Impact, nicht die technische Implementierung.
