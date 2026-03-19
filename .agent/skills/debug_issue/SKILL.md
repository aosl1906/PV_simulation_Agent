---
name: debug_issue
description: Systematische Fehlersuche (Reproduktion → Root Cause → Fix → Verifikation)
---

# Skill: Fehler debuggen

## Prozess

Debugging ist kein Raten. Es ist ein strukturierter Prozess in vier Phasen.

```
Reproduzieren → Root Cause → Fix → Verifikation
```

---

## Phase 1: Reproduzieren

**Ziel:** Den Fehler zuverlässig und kontrolliert auslösen.

1. Fehlerbeschreibung des Users vollständig verstehen:
   - Was sollte passieren?
   - Was passiert stattdessen?
   - Wann passiert es? (immer / manchmal / unter bestimmten Bedingungen)

2. Fehler selbst reproduzieren:
   - Den exakt gleichen Schritt ausführen wie der User.
   - Fehlermeldung / Stack Trace vollständig lesen.

3. Falls der Fehler nicht reproduzierbar ist:
   - User um mehr Kontext bitten (Logs, Screenshots, Browser-Konsole).
   - Edge-Cases prüfen (leere Eingaben, Netzwerkfehler, Race Conditions).

---

## Phase 2: Root Cause finden

**Ziel:** Die Ursache identifizieren, nicht nur das Symptom.

**Vorgehen:**
1. Fehlermeldung / Stack Trace lesen – wo genau bricht es?
2. Den betroffenen Code-Pfad zurückverfolgen.
3. Hypothesen formulieren (mindestens 2–3 mögliche Ursachen).
4. Hypothesen systematisch eingrenzen (via Logs, gezielten Prints, Tests).

**Häufige Ursachen:**
- Falsche Annahmen über Datentypen oder Null-Werte
- Zustandsprobleme (State zu früh / zu spät aktualisiert)
- Timing-Probleme (Race Conditions, Async/Await-Fehler)
- Falsche Umgebungsvariablen oder fehlende Konfiguration
- Breaking Changes an externen APIs oder Dependencies

---

## Phase 3: Fix

**Ziel:** Die Ursache beheben, nicht das Symptom unterdrücken.

1. Nur die minimal notwendige Änderung vornehmen.
2. Den Fix dokumentieren: Kurzkommentar warum die Änderung nötig war.
3. `/check_syntax` ausführen.
4. `/run_tests` ausführen.

**Anti-Patterns:**
- ❌ Try-Catch um den Fehler herum, ohne die Ursache zu beheben.
- ❌ Schlaflose Schleifen statt richtiger asynchroner Logik.
- ❌ Hardcoded Dummy-Werte zum Kaschieren von Berechnungsfehlern.

---

## Phase 4: Verifikation

1. Den ursprünglichen Bug-Schritt des Users erneut durchführen.
2. Bestätigen: Fehler tritt nicht mehr auf.
3. Seiteneffekte prüfen: Hat der Fix andere Teile des Systems beeinflusst?
4. Regression-Test schreiben (wenn es sich um einen kritischen Bug handelt).

---

## Abschluss

- `CHANGELOG.md` aktualisieren: `fix: [kurze Beschreibung des behobenen Fehlers]`
- Commit nach folgendem Muster: `fix: [beschreibung]`
- User informieren: Was war die Ursache, was wurde geändert.
