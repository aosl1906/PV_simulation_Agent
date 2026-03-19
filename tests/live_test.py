"""
Live-Test: Alle 4 MCP Tools gegen das laufende PV Backend testen.
Führe aus mit: python tests/live_test.py
"""
import asyncio
import sys
import os
import json

# Projekt-Root zum Python-Path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.http_client import check_backend_health
from src.tools.geocode import geocode_address
from src.tools.simulate import build_simulation_request, run_simulation


async def main():
    print("=" * 60)
    print("PV Simulation Agent — Live-Test")
    print("=" * 60)

    # --- Test 1: Backend Health Check ---
    print("\n🔍 Test 1: Backend Health Check...")
    healthy = await check_backend_health()
    print(f"   Ergebnis: {'✅ Erreichbar' if healthy else '❌ Nicht erreichbar'}")
    if not healthy:
        print("   ⛔ Abbruch: Backend muss laufen!")
        return

    # --- Test 2: Geocoding ---
    print("\n🔍 Test 2: Geocoding 'München'...")
    geo = await geocode_address("München, Deutschland")
    if "error" in geo:
        print(f"   ❌ Fehler: {geo['error']}")
        return
    lat, lon = geo["latitude"], geo["longitude"]
    print(f"   ✅ {geo['display_name']}")
    print(f"   📍 lat={lat:.4f}, lon={lon:.4f}")

    # --- Test 3: Simulation ---
    print("\n🔍 Test 3: Simulation (10 kWp, Süddach, 10 kWh Batterie, München)...")
    request = build_simulation_request(
        latitude=lat,
        longitude=lon,
        arrays=[{
            "name": "Süddach",
            "tilt": 30,
            "azimuth": 180,
            "peak_power_kw": 10.0,
        }],
        battery_capacity_kwh=10.0,
        annual_consumption_kwh=5000.0,
    )
    print(f"   Request-Keys: {list(request.keys())}")
    print(f"   Arrays: {request['arrays']}")

    result = await run_simulation(request)

    if "error" in result:
        print(f"   ❌ Fehler: {result['error']}")
        return

    print(f"   ✅ Simulation erfolgreich!")
    print()
    print(result["summary_text"])

    # Raw Summary Details
    raw = result.get("raw_summary", {})
    if raw:
        print(f"\n   📊 Raw Summary Keys: {list(raw.keys())}")

    print("\n" + "=" * 60)
    print("✅ ALLE TESTS BESTANDEN")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
