# Architektur-Entscheidungen (ADR)

> **Projekt:** _[Projektname]_  
> **Format:** Architectural Decision Records (ADR)

Dieses Dokument hält alle wesentlichen technischen Entscheidungen fest – mit Kontext, Alternativen und Begründung. So kann jeder (Mensch oder Agent) nachvollziehen, **warum** etwas so gebaut wurde.

---

## Vorlage

```
## ADR-[NNN]: [Titel]

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-NNN

**Kontext:**
[Was ist die Situation? Was ist das Problem, das gelöst werden muss?]

**Entscheidung:**
[Was wurde entschieden?]

**Alternativen:**
- Option A: [Beschreibung] – [Warum nicht gewählt?]
- Option B: [Beschreibung] – [Warum nicht gewählt?]

**Konsequenzen:**
- Positiv: [Vorteile der Entscheidung]
- Negativ: [Nachteile / Kompromisse / Schulden]

**Datum:** YYYY-MM-DD
```

---

## ADR-001: Tech-Stack Wahl

**Status:** Accepted

**Kontext:**
_[Warum wurde dieser Tech-Stack für das Projekt gewählt?]_

**Entscheidung:**
_[Gewählter Stack: z.B. React/Vite + FastAPI + PostgreSQL]_

**Alternativen:**
- _[Alternative A]_: _[Warum nicht gewählt?]_
- _[Alternative B]_: _[Warum nicht gewählt?]_

**Konsequenzen:**
- Positiv: _[Vorteile]_
- Negativ: _[Nachteile]_

**Datum:** _[Datum]_

---

<!-- SETUP: Weitere ADRs nach dem gleichen Muster hier einfügen. -->
<!-- Typische Kandidaten für ADRs: Datenbank-Wahl, Auth-Strategie, Deployment-Plattform, Testing-Ansatz -->

*Neue Entscheidungen werden laufend ergänzt. Antigravity fügt bei grundlegenden Design-Entscheidungen proaktiv einen ADR-Eintrag ein und speichert den Kern der Entscheidung sofort im **Memory MCP**.*
