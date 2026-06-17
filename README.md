# 🚦 AI-Powered Parking Violation Intelligence System

## Overview

This project analyzes parking violation data from Bengaluru and transforms raw traffic enforcement records into actionable intelligence for traffic police departments.

The system identifies high-risk junctions, predicts emerging violation hotspots, recommends resource allocation strategies, and visualizes city-wide violation patterns through an interactive dashboard.

---

## Dataset

* Total Violations: 298,450
* Locations Analyzed: 10,942
* Junctions Monitored: 169
* Police Stations Covered: 54

---

## Key Features

### Hotspot Detection

Identifies violation-prone junctions and police station zones.

### Risk Scoring Engine

Calculates risk scores based on:

* Violation volume
* Weekend activity
* Peak-hour concentration

### Resource Allocation Recommendation

Provides enforcement recommendations such as:

* Additional officers
* Patrol vehicles
* Towing support
* Routine monitoring

### Future Hotspot Prediction

Forecasts junctions with increasing parking violations.

### Geographic Cluster Analysis

Uses K-Means clustering to identify city-wide violation concentration zones.

### Interactive Dashboard

Built using Streamlit for real-time exploration and decision support.

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Folium
* Streamlit

---

## Results

### High-Risk Junctions

1. BTP051 - Safina Plaza Junction
2. BTP082 - KR Market Junction
3. BTP040 - Elite Junction
4. BTP044 - Sagar Theatre Junction

### Future Emerging Hotspots

* Sagar Theatre Junction
* Mahalaxmi Layout Entrance
* Dr. Rajkumar Road Junction
* Subbanna Junction

---

## Run Locally

Install dependencies:

pip install -r requirements.txt

Launch dashboard:

streamlit run app.py

---

## Impact

The system enables proactive traffic enforcement by helping authorities:

* Reduce illegal parking
* Improve traffic flow
* Optimize officer deployment
* Identify future violation hotspots
* Support data-driven urban mobility planning
