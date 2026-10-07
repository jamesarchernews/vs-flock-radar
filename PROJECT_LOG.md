# THE VALLEY STAR | INVESTIGATIVE DATA DESK
Project: San Fernando Valley ALPR Civic Transparency Map (VS-FlockRadar)
Lead Reporter / Architect: James Atlas Archer
Affiliation: The Valley Star | Los Angeles Valley College
Status: Standalone Production Build 1.0 (Public Reader Edition)

================================================================================
1. EDITORIAL & CIVIC PURPOSE
================================================================================
Across the San Fernando Valley, municipal police departments (LAPD Valley Bureau, 
Burbank PD, San Fernando PD) and private homeowner associations have deployed 
Automated License Plate Readers (ALPRs)—primarily manufactured by Flock Safety.

These networks record vehicular movements, timestamps, and travel directions. 
While cited for property and auto theft investigations, data sharing arrangements 
often extend beyond immediate municipal borders with limited public transparency.

VS-FlockRadar is a public-service transparency dashboard designed specifically for 
Valley Star readers, LAVC students, and community members to:
- View known, verified Flock camera locations across the San Fernando Valley.
- Identify camera operators (city, police department, transit, or private HOA).
- Understand surveillance density along key commuter and campus corridors.

================================================================================
2. TECHNICAL ARCHITECTURE & OSINT DATA SOURCES
================================================================================
- Independent Root: Completely uncoupled from internal newsroom tactical engines.
- Upstream Telemetry Sources:
  * DeFlock Project (FoggedLens/deflock) & OpenStreetMap Overpass API:
    Queries tag specifications:
    - surveillance:type=ALPR
    - camera:type=alpr
    - operator matches (Flock Safety, LAPD, Burbank, Glendale, LASD, etc.)
  * National Flock Dataset audits (FlockLocations & simeononsecurity/flock-finder)
- Geospatial Filtering (San Fernando Valley Basin):
  * Latitude: 34.1200° N (Studio City / Woodland Hills) to 34.3500° N (Sylmar / San Fernando)
  * Longitude: -118.6800° W (Chatsworth / West Hills) to -118.3000° W (Burbank / Glendale)

================================================================================
3. DESIGN STANDARDS (LAVC BRAND GUIDELINES 2022)
================================================================================
Built to comply with Los Angeles Valley College visual identity standards:
- Primary Accent: Valley Gold (#FCB926) — Camera nodes, active pulses, alerts
- Primary Branding: Valley Green (#20680C) — Masthead badges, active tabs
- Card Surfaces: Monarch Green (#00513F) — Sidebar panels and metric containers
- Borders & Dividers: Shaded Green (#2F3F3A) — Contrast outlines and layout dividers
- Telemetry Highlights: Lion's Mane (#FFE2A5) — Coordinate stats and secondary tags

================================================================================
4. READER PRIVACY ASSURANCE
================================================================================
- Zero reader location tracking.
- Zero third-party behavioral cookies.
- Client-side static rendering for instantaneous mobile loading.
================================================================================
