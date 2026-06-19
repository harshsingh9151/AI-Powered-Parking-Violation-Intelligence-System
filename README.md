# 🚦 ParkSight AI

### Intelligent Parking Violation Hotspot Detection and Enforcement Prioritization System

## Overview

ParkSight AI is a data-driven traffic enforcement intelligence platform that helps authorities identify parking violation hotspots, predict emerging congestion zones, and optimize enforcement resource allocation.

The system analyzes large-scale parking violation records and transforms them into actionable insights through hotspot detection, risk scoring, future hotspot prediction, geographic clustering, and interactive visualization.

---

## Problem Statement

Parking-induced congestion is a major contributor to urban traffic inefficiency. Traffic authorities often lack visibility into:

* High-risk violation locations
* Emerging congestion hotspots
* Enforcement resource requirements
* Spatial violation patterns

This leads to reactive enforcement instead of proactive intervention.

---

## Solution

ParkSight AI provides:

✅ Parking Violation Hotspot Detection

✅ Junction Risk Scoring

✅ Future Hotspot Prediction

✅ Enforcement Resource Allocation Recommendations

✅ Geographic Cluster Analysis

✅ Interactive Decision Support Dashboard

---

## Dataset Summary

| Metric             | Value   |
| ------------------ | ------- |
| Total Violations   | 298,450 |
| Junctions Analyzed | 168     |
| Locations Covered  | 10,942  |
| Police Stations    | 54      |

---

## Key Features

### 1. Hotspot Detection

Identifies junctions with the highest concentration of parking violations.

### 2. Risk Scoring Engine

Each junction is assigned a risk score using:

* Total violations
* Weekend activity rate
* Peak-hour activity rate

### 3. Future Hotspot Prediction

Predicts emerging parking violation hotspots using trend-based forecasting.

### 4. Resource Allocation

Provides actionable recommendations:

| Risk Level | Recommendation                           |
| ---------- | ---------------------------------------- |
| High       | 4 Officers + Towing Vehicle + Barricades |
| Medium     | 2 Officers                               |
| Low        | Routine Monitoring                       |

### 5. Geographic Clustering

Uses K-Means clustering to identify violation concentration zones across the city.

---

## Top High-Risk Junctions

| Junction               | Risk Score |
| ---------------------- | ---------- |
| Safina Plaza Junction  | 79.44      |
| KR Market Junction     | 62.26      |
| Elite Junction         | 56.89      |
| Sagar Theatre Junction | 56.29      |

---

## Emerging Future Hotspots

| Junction                  | Growth Forecast |
| ------------------------- | --------------- |
| Dr. Rajkumar Road         | +53.8%          |
| Sagar Theatre Junction    | +52.8%          |
| Mahalaxmi Layout Entrance | +50.6%          |
| AS Char Street            | +50.0%          |

---

## Dashboard

The Streamlit dashboard provides:

* KPI Overview
* Risk Analysis
* Future Hotspot Prediction
* Resource Allocation
* Geographic Cluster Visualization

### Live Demo

https://ai-powered-parking-violation-intelligence-system.streamlit.app/

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Folium
* Scikit-Learn
* Streamlit

---

## Project Structure

```text
app.py

data/
├── junction_risk_summary.csv
├── future_hotspot_predictions.csv

assets/
├── top_risk_junctions.png
├── future_hotspots.png
├── risk_distribution.png
├── resource_allocation.png

maps/
└── cluster_map.html
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/harshsingh9151/AI-Powered-Parking-Violation-Intelligence-System.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Impact

ParkSight AI enables traffic authorities to:

* Reduce parking-induced congestion
* Improve traffic flow
* Optimize officer deployment
* Prioritize high-risk areas
* Make data-driven enforcement decisions

---

## Future Enhancements

* Machine Learning-based forecasting
* Real-time violation monitoring
* Integration with CCTV systems
* Dynamic enforcement scheduling
* Smart city integration

---

## Team

Harsh Singh

National Institute of Technology Calicut

Prototype Round 2 Submission
