---
description: Neues Projekt auf Basis des Templates einrichten
---

# /new_project_setup

Führt das vollständige Setup-Gespräch für ein neues Projekt durch.

## Schritte

1. **SETUP_GUIDE.md lesen:**
   - Öffne und lies `SETUP_GUIDE.md` vollständig.
   - Stelle dem User die Fragen aus Phase 1–5 **nacheinander** (nicht alle auf einmal).
   - Dokumentiere jede Antwort sofort im entsprechenden Dokument.

2. **gemini.md befüllen:**
   - Alle `<!-- SETUP: ... -->` Blöcke ersetzen.
   - Setup-Kommentare nach dem Ausfüllen entfernen.

3. **docs/architecture.md befüllen:**
   - Tech-Stack eintragen.
   - Projektspezifische Schichtaufteilung dokumentieren.

4. **env_reference.md befüllen:**
   - Alle Umgebungsvariablen und Ports eintragen.

5. **dev_start.md befüllen:**
   - Konkrete Startbefehle eintragen, `// turbo` Annotationen prüfen.

6. **README.md anpassen:**
   - Projektname, Beschreibung, Voraussetzungen, Start-Anleitung.

7. **SETUP_GUIDE.md löschen oder archivieren:**
   - Nach vollständigem Setup kann die Datei entfernt werden.

8. **Initialen Commit erstellen:**
   ```powershell
   git add .
   git commit -m "feat: initial project setup from template"
   ```

## Ergebnis

Das Projekt ist vollständig konfiguriert und bereit für die erste Feature-Entwicklung.
Nächster Schritt: `/dev_start` ausführen und das Projekt zum Leben erwecken.
