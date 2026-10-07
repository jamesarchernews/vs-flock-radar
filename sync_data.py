import json
import urllib.request
import urllib.parse
import os
import time

# San Fernando Valley strict bounding box
SFV_BBOX = {
    "lamin": 34.1200, "lamax": 34.3500, "lomin": -118.6800, "lomax": -118.3000
}

def in_sfv(lon, lat):
    try:
        return SFV_BBOX["lomin"] <= float(lon) <= SFV_BBOX["lomax"] and SFV_BBOX["lamin"] <= float(lat) <= SFV_BBOX["lamax"]
    except Exception:
        return False

collected_cameras = []
seen_ids = set()

def add_feature(lon, lat, props):
    coord_key = f"{round(lon, 4)}_{round(lat, 4)}"
    if coord_key not in seen_ids:
        seen_ids.add(coord_key)
        collected_cameras.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [float(lon), float(lat)]},
            "properties": props
        })

HEADERS = {"User-Agent": "ValleyStar-FlockRadar/2.0"}

print("[*] STEP 1: Attempting simeononsecurity/flock-finder Datasets...")
GH_URLS = [
    "https://raw.githubusercontent.com/simeononsecurity/flock-finder/master/data/flock_cameras.geojson",
    "https://raw.githubusercontent.com/simeononsecurity/flock-finder/main/data/flock_cameras.geojson"
]

for url in GH_URLS:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for feat in data.get("features", []):
                coords = feat.get("geometry", {}).get("coordinates", [])
                if len(coords) >= 2 and in_sfv(coords[0], coords[1]):
                    props = feat.get("properties", {})
                    add_feature(coords[0], coords[1], {
                        "id": props.get("id", "flock_node"),
                        "name": props.get("name", "Fixed ALPR Checkpoint"),
                        "operator": props.get("operator", "Flock Safety / Regional PD"),
                        "brand": "Flock Safety",
                        "mount": props.get("mount", "Utility Pole"),
                        "direction": props.get("direction", "Roadway Facing"),
                        "verified": "Flock-Finder Telemetry"
                    })
            print(f"  [✓] Success with {url}")
            break
    except Exception:
        pass

print(f"[*] STEP 2: Querying OpenStreetMap via Overpass (Grid-Chunking)...")
# Splitting SFV into 4 quadrants to prevent Overpass 504 Gateway Timeouts
GRIDS = [
    (34.1200, -118.6800, 34.2350, -118.4900), # Southwest SFV (e.g. Chatsworth/Woodland Hills)
    (34.1200, -118.4900, 34.2350, -118.3000), # Southeast SFV (e.g. Studio City/Burbank)
    (34.2350, -118.6800, 34.3500, -118.4900), # Northwest SFV (e.g. Northridge/Granada Hills)
    (34.2350, -118.4900, 34.3500, -118.3000)  # Northeast SFV (e.g. Sylmar/Pacoima)
]

for i, (lamin, lomin, lamax, lomax) in enumerate(GRIDS):
    query = f"""[out:json][timeout:25];(
      nwr["surveillance:type"="ALPR"]({lamin},{lomin},{lamax},{lomax});
      nwr["camera:type"="alpr"]({lamin},{lomin},{lamax},{lomax});
    );out center;"""
    encoded_data = urllib.parse.urlencode({'data': query}).encode('utf-8')
    req = urllib.request.Request("https://overpass-api.de/api/interpreter", data=encoded_data, headers=HEADERS)
    
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            payload = json.loads(resp.read().decode('utf-8'))
            elements = payload.get("elements", [])
            for el in elements:
                lat = el.get("lat") or el.get("center", {}).get("lat")
                lon = el.get("lon") or el.get("center", {}).get("lon")
                tags = el.get("tags", {})
                if lat and lon:
                    add_feature(lon, lat, {
                        "id": el.get("id"),
                        "name": tags.get("name", "Fixed ALPR Checkpoint"),
                        "operator": tags.get("operator", tags.get("agency", "Regional Agency / HOA")),
                        "brand": tags.get("brand", "Flock Safety"),
                        "mount": tags.get("camera:mount", "Utility Pole / Mast"),
                        "direction": tags.get("camera:direction", "Roadway Facing"),
                        "verified": "OpenStreetMap / DeFlock"
                    })
        print(f"  [✓] Quadrant {i+1}/4 cleared.")
    except Exception as e:
        print(f"  [!] Quadrant {i+1}/4 failed: {e}")
    time.sleep(1) # Be polite to Overpass API to prevent rate limits

if len(collected_cameras) > 0:
    os.makedirs("data", exist_ok=True)
    out_file = os.path.join("data", "sfv_flock.geojson")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": collected_cameras}, f, indent=2)
    print(f"\n[✓] SUCCESS: Extracted and saved {len(collected_cameras)} unique SFV ALPR nodes.")
else:
    print("\n[!] Could not extract any data from Github or Overpass.")
