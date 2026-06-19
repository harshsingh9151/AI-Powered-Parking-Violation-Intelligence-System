import streamlit as st
import pandas as pd
import os

st.set_page_config(
page_title="AI Parking Intelligence",
page_icon="🚦",
layout="wide"
)

st.title("🚦 AI-Powered Parking Violation Intelligence System")

st.subheader("Smart Traffic Enforcement Dashboard")

risk = pd.read_csv("data/junction_risk_summary.csv")
future = pd.read_csv("data/future_hotspot_predictions.csv")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Violations", "298,450")
col2.metric("Locations", "10,942")
col3.metric("Junctions", "168")
col4.metric("Police Stations", "54")

st.divider()

st.header("⚠️ Top Risk Junctions")

if os.path.exists("assets/top_risk_junctions.png"):
st.image("assets/top_risk_junctions.png")

st.header("🔮 Future Hotspots")

if os.path.exists("assets/future_hotspots.png"):
st.image("assets/future_hotspots.png")

st.header("📊 Risk Distribution")

if os.path.exists("assets/risk_distribution.png"):
st.image("assets/risk_distribution.png")

st.header("👮 Resource Allocation")

if os.path.exists("assets/resource_allocation.png"):
st.image("assets/resource_allocation.png")

st.header("📋 Junction Risk Summary")

st.dataframe(
risk.sort_values(
"risk_score",
ascending=False
),
use_container_width=True
)

st.header("📈 Emerging Hotspots")

st.dataframe(
future.sort_values(
"growth_percent",
ascending=False
),
use_container_width=True
)

st.header("🗺️ Cluster Analysis Map")

if os.path.exists("maps/cluster_map.html"):

```
with open(
    "maps/cluster_map.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

st.components.v1.html(
    html,
    height=700,
    scrolling=True
)
```

else:
st.warning("cluster_map.html not found")
