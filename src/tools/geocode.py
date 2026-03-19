"""
Module: src/tools/geocode.py

Beschreibung:
    Geocoding-Tool: Konvertiert Adressen/Städtenamen in Koordinaten (lat/lon)
    über die kostenlose Nominatim API (OpenStreetMap).

Hinweis:
    Nominatim hat ein Rate-Limit von 1 Request/Sekunde.
    Für den Agent-Einsatz völlig ausreichend.
"""
import httpx
import logging

logger = logging.getLogger("mcp.tools.geocode")

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
USER_AGENT = "PVSimulationAgent/1.0"


async def geocode_address(address: str) -> dict:
    """
    Konvertiert eine Adresse oder einen Stadtnamen in Koordinaten.

    Args:
        address: Freitext-Adresse (z.B. "München" oder "Musterstraße 1, 80331 München")

    Returns:
        Dict mit 'latitude', 'longitude', 'display_name' oder 'error'
    """
    logger.info(f"Geocoding: '{address}'")

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                NOMINATIM_URL,
                params={
                    "q": address,
                    "format": "json",
                    "limit": 1,
                    "addressdetails": 1,
                },
                headers={"User-Agent": USER_AGENT},
            )
            response.raise_for_status()
            results = response.json()

        if not results:
            return {"error": f"Adresse nicht gefunden: '{address}'"}

        result = results[0]
        lat = float(result["lat"])
        lon = float(result["lon"])
        display_name = result.get("display_name", address)

        logger.info(f"Gefunden: {display_name} → ({lat:.4f}, {lon:.4f})")

        return {
            "latitude": lat,
            "longitude": lon,
            "display_name": display_name,
        }

    except Exception as e:
        logger.error(f"Geocoding fehlgeschlagen: {e}", exc_info=True)
        return {"error": f"Geocoding fehlgeschlagen: {str(e)}"}
