# 📡 Valley Star ALPR Surveillance Grid

**Developed by:** James Atlas Archer | Online Editor, The Valley Star  
**Project Output:** OSINT Tactical HUD / ALPR Tracking Dashboard  
**Presented At:** Journalism Association of Community Colleges (JACC) SoCal Conference 2026

## 🗄️ Project Overview
This interactive data journalism tool maps the proliferation of Automated License Plate Readers (ALPRs) across Greater Los Angeles. Built to support investigative reporting for *The Valley Star*, the dashboard utilizes a custom tactical UI to visualize surveillance density, hardware types, and operator telemetry.

## ⚖️ Legal & Ethical Disclosure
*   **Public Data Only:** This tool operates strictly on publicly available, crowdsourced Open-Source Intelligence (OSINT).
*   **No Proprietary Access:** This application **does not** interface with, query, or access any law enforcement, municipal, or private corporate databases (e.g., Flock Safety backend systems). 
*   **First Amendment Protection:** Data visualization of public infrastructure in plain view is conducted under standard journalistic news-gathering protections.
*   **Accuracy Disclaimer:** Node coordinates are sourced from OpenStreetMap contributors and DeFlock community telemetry. *The Valley Star* does not guarantee the real-time operational status of individual cameras.

## 🛠️ Methodology & Tech Stack
*   **Data Aggregation:** Queries OpenStreetMap (OSM) via the Overpass API, utilizing an 8-sector grid-chunking script to bypass regional bounding box timeouts and parse thousands of nodes across Greater LA.
*   **Map Engine:** Leaflet.js rendering OpenStreetMap tiles with custom high-contrast CSS inversion to bypass commercial API rate limits while maintaining high-resolution topological details.
*   **Data Formatting:** Raw telemetry is parsed into GeoJSON feature collections, clustered dynamically based on viewport zoom, and injected into a custom HTML/Tailwind CSS tactical interface.

## 📝 Developer Logs
*   **v1.0.0:** Initial repository build and Overpass API integration.
*   **v1.1.0:** Deployed grid-chunking to stabilize SFV bounding box timeouts.
*   **v2.0.0:** Replaced standard markers with tactical clustering and directional Field-of-View (FoV) radar cones.
*   **v2.1.0:** Migrated map engine and deployed live via Render for JACC presentation.
*   **v3.0.0:** Expanded telemetry extraction footprint to the Greater Los Angeles region, integrating 8-sector grid-chunking for massive regional scaling.
