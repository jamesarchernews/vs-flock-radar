# 📡 Valley Star ALPR Surveillance Grid

**Developed by:** James Atlas Archer | Online Editor, The Valley Star  
**Project Output:** OSINT Tactical HUD / ALPR Tracking Dashboard  
**Presented At:** (TBD)

## 🗄️ Project Overview
This interactive data journalism tool maps the proliferation of Automated License Plate Readers (ALPRs) across Greater Los Angeles. Built to support investigative reporting for *The Valley Star*, the dashboard utilizes a custom tactical UI to visualize surveillance density, hardware types, and operator telemetry.

## ⚖️ Legal & Privacy Protections
*   **Zero-PII Architecture:** This platform indexes **fixed public hardware only**. It collects, processes, and displays **zero Personally Identifiable Information (PII)**. No vehicle registrations, driver identities, or live license plate reads are ever captured or stored.
*   **California SB 34 Alignment:** Implemented in accordance with California Senate Bill 34 standards advocating public transparency for automated license plate reader deployments.
*   **First Amendment Doctrine:** Physical recording and mapping of surveillance equipment installed on public rights-of-way and utility poles in plain sight constitutes protected newsgathering.
*   **Crowdsourced Verification:** Coordinates are gathered from OpenStreetMap contributors and DeFlock telemetry. Real-time operational uptime is not guaranteed.

## 🛠️ Methodology & Technical Stack
*   **Data Aggregation:** Queries OpenStreetMap (OSM) via Overpass API with an 8-sector grid-chunking protocol to eliminate server timeouts across Greater LA.
*   **Map Rendering:** Leaflet.js with dynamic Marker Clustering and inverted high-contrast raster tiles for high-resolution street legibility.
*   **Civic Open Data:** Node telemetry is exported in open GeoJSON format to facilitate academic and civic oversight.

## 📄 License
This project and dataset are published under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. Non-commercial civic, academic, and journalistic reproduction is permitted with attribution.
