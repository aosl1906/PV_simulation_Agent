"""
Module: src/utils/http_client.py

Beschreibung:
    Zentraler HTTP-Client für alle Anfragen an das PV Simulation Backend.
    Nutzt httpx (async) mit konfigurierbarer Base-URL und sinnvollen Timeouts.

Konfiguration:
    - PV_SIM_BACKEND_URL: aus .env oder Umgebungsvariable (default: http://localhost:8000)
"""
import os
import httpx
import logging

logger = logging.getLogger("mcp.http_client")

# Simulation kann 30+ Sekunden dauern (8760h Dispatch Loop)
DEFAULT_TIMEOUT = httpx.Timeout(
    connect=5.0,
    read=120.0,   # Simulation: bis zu 2 Minuten bei komplexen Szenarien
    write=10.0,
    pool=5.0,
)


def get_backend_url() -> str:
    """Gibt die konfigurierte Backend-URL zurück."""
    return os.getenv("PV_SIM_BACKEND_URL", "http://localhost:8000")


async def post_json(endpoint: str, payload: dict, timeout: httpx.Timeout | None = None) -> dict:
    """
    Sendet einen POST-Request mit JSON-Body an das PV Backend.

    Args:
        endpoint: API-Pfad (z.B. "/simulate")
        payload: JSON-Body als dict
        timeout: Optional, überschreibt den Default-Timeout

    Returns:
        Response-Body als dict

    Raises:
        httpx.HTTPStatusError: Bei HTTP-Fehlern (4xx/5xx)
        httpx.ConnectError: Wenn Backend nicht erreichbar
    """
    url = f"{get_backend_url()}{endpoint}"
    logger.info(f"POST {url} (Payload-Größe: {len(str(payload))} Zeichen)")

    async with httpx.AsyncClient(timeout=timeout or DEFAULT_TIMEOUT) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        return response.json()


async def get_json(endpoint: str) -> dict:
    """
    Sendet einen GET-Request an das PV Backend.

    Args:
        endpoint: API-Pfad (z.B. "/")

    Returns:
        Response-Body als dict
    """
    url = f"{get_backend_url()}{endpoint}"

    async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


async def check_backend_health() -> bool:
    """Prüft ob das PV Simulation Backend erreichbar ist."""
    try:
        result = await get_json("/")
        logger.info(f"Backend erreichbar: {result.get('message', 'OK')}")
        return True
    except Exception as e:
        logger.warning(f"Backend nicht erreichbar: {e}")
        return False
