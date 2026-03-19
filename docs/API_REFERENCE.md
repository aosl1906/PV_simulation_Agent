# API-Referenz

> **Projekt:** _[Projektname]_  
> **Basis-URL:** _[z.B. http://localhost:8000 (lokal) / https://api.projekt.de (Produktion)]_

<!-- SETUP: Falls kein Backend/keine API vorhanden: Diese Datei löschen und aus docs/ entfernen. -->

---

## Authentifizierung

<!-- SETUP: Authentifizievungsverfahren eintragen oder "Keine Authentifizierung" angeben. -->

| Methode | Beschreibung |
|---|---|
| _[z.B. Bearer Token]_ | _[Token im `Authorization: Bearer <token>` Header]_ |
| _[z.B. API-Key]_ | _[Key als Query-Parameter oder Header]_ |
| Keine | _[Öffentliche API ohne Authentifizierung]_ |

---

## Endpunkte

<!-- SETUP: Alle API-Endpunkte dokumentieren. Vorlage pro Endpunkt unten. -->

### `POST /[endpoint]`

**Beschreibung:** _[Was macht dieser Endpunkt?]_

**Request Body:**
```json
{
  "[feld_1]": "[Typ | Beschreibung]",
  "[feld_2]": "[Typ | Beschreibung]"
}
```

**Response (200 OK):**
```json
{
  "[ergebnis_feld]": "[Typ | Beschreibung]"
}
```

**Fehlercodes:**
| Code | Bedeutung |
|---|---|
| `400` | Ungültige Eingabe |
| `422` | Validierungsfehler (Schema) |
| `500` | Serverfehler |

---

### `GET /[endpoint]/{id}`

**Beschreibung:** _[Was macht dieser Endpunkt?]_

**Parameter:**
| Name | Typ | Pflicht | Beschreibung |
|---|---|---|---|
| `id` | String | ✅ | _[Beschreibung]_ |
| `[query_param]` | Boolean | ⬜ | _[Beschreibung]_ |

**Response (200 OK):**
```json
{
  "[feld]": "[Wert]"
}
```

---

<!-- VORLAGE: Weitere Endpunkte hier nach dem gleichen Muster einfügen. -->

---

## Datentypen & Schemas

<!-- SETUP: Gemeinsame Datentypen dokumentieren, die in mehreren Endpunkten vorkommen. -->

### `[SchemaName]`

```json
{
  "id": "string (UUID)",
  "[feld]": "[Typ]",
  "created_at": "ISO 8601 Timestamp"
}
```

---

*Diese Datei wird bei jeder API-Änderung aktualisiert (Skill: `update_docs`).*
