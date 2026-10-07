# THE VALLEY STAR | INVESTIGATIVE DATA DESK
Project: Greater Los Angeles ALPR Civic Transparency Map (VS-FlockRadar)
Lead Reporter / Architect: James Atlas Archer
Affiliation: The Valley Star | Los Angeles Valley College
Status: Standalone Production Build 3.1 (JACC Public Reader Edition)

================================================================================
1. EDITORIAL & CIVIC PURPOSE
================================================================================
Across the Greater Los Angeles region, municipal police departments and private 
homeowner associations have deployed Automated License Plate Readers (ALPRs)—
primarily manufactured by Flock Safety.

These networks record vehicular movements, timestamps, and travel directions. 
While cited for property and auto theft investigations, data sharing arrangements 
often extend beyond immediate municipal borders with limited public transparency.

VS-FlockRadar is a public-service transparency dashboard designed specifically for 
Valley Star readers, LAVC students, and community members to:
- View known, verified surveillance camera locations across Greater LA, from Ventura to Orange County.
- Filter and identify camera operators (Municipal Police/City vs. Private HOA/Commercial).
- Understand surveillance density along key commuter and campus corridors.
- Download verified open-source datasets for independent civic research.

================================================================================
2. TECHNICAL ARCHITECTURE & OSINT DATA SOURCES
================================================================================
- Independent Root: Completely uncoupled from internal newsroom tactical engines.
- Upstream Telemetry Sources:
  * DeFlock Project & OpenStreetMap Overpass API:
    - Custom 8-sector grid-chunking protocol to eliminate server timeouts.
    - Queries tag specifications: surveillance:type=ALPR, camera:type=alpr, surveillance=outdoor
  * National Flock Dataset audits (FlockLocations & simeononsecurity/flock-finder)
- Map Engine: Leaflet.js with OpenStreetMap (OSM) raster tiles, utilizing a high-contrast CSS 
  inversion filter to render a tactical dark-mode topology without triggering commercial API limits.
- Geospatial Filtering (Greater L.A. Basin):
  * Latitude: 33.4000° N to 34.8000° N
  * Longitude: -119.2000° W to -117.2000° W

================================================================================
3. DESIGN STANDARDS (LAVC BRAND GUIDELINES)
================================================================================
Built to comply with Los Angeles Valley College visual identity standards while 
maintaining an OSINT tactical aesthetic:
- Primary Accent: Valley Gold (#FCB926) — Camera nodes, radar cones, alerts
- Primary Branding: Valley Green (#20680C) — Masthead badges
- Card Surfaces: Monarch Green (#00513F) / Obsidian (#040605) — HUD panels
- Borders & Dividers: Teal Green (#307F6A) — Contrast outlines and layout dividers
- Telemetry Highlights: Lion's Mane (#FFE2A5) — Coordinate stats and secondary tags

================================================================================
4. LEGAL SHIELDS & READER PRIVACY ASSURANCE
================================================================================
- Zero-PII Mandate: The platform tracks fixed public hardware only. Zero Personally 
  Identifiable Information (PII) is captured, stored, or displayed.
- California SB 34 Alignment: Operates in accordance with state guidelines promoting 
  transparency of ALPR usage.
- First Amendment Protection: Visualizing physical equipment in plain view on 
  public rights-of-way constitutes protected newsgathering activity.
- Zero reader location tracking or third-party behavioral cookies.
- License: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
================================================================================
