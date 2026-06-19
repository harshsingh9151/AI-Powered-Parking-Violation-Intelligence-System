import streamlit as st
import pandas as pd
import os

st.set\_page\_config(
page\_title="AI Parking Intelligence",
layout="wide"
)

st.title("🚦 AI-Powered Parking Violation Intelligence System")

st.markdown(
"""
Smart Traffic Enforcement & Parking Intelligence Dashboard
"""
)

# ==========================

# KPI SECTION

# ==========================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
"Total Violations",
"298,450"
)

col2.metric(
"Monitored Junctions",
"168"
)

col3.metric(
"Priority Junctions",
"16"
)

col4.metric(
"Critical Junctions",
"4"
)

st.divider()

# ==========================

# RISK CHART

# ==========================

st.header("⚠️ Top Risk Junctions")

if os.path.exists("assets/top\_risk\_junctions.png"):
st.image("assets/top\_risk\_junctions.png")
else:
st.warning("top\_risk\_junctions.png not found")

# ==========================

# FUTURE HOTSPOTS

# ==========================

st.header("🔮 Future Hotspot Prediction")

if os.path.exists("assets/future\_hotspots.png"):
st.image("assets/future\_hotspots.png")
else:
st.warning("future\_hotspots.png not found")

# ==========================

# RISK DISTRIBUTION

# ==========================

st.header("📊 Risk Distribution")

if os.path.exists("assets/risk\_distribution.png"):
st.image("assets/risk\_distribution.png")
else:
st.warning("risk\_distribution.png not found")

# ==========================

# RESOURCE ALLOCATION

# ==========================

st.header("👮 Recommended Enforcement Allocation")

if os.path.exists("assets/resource\_allocation.png"):
st.image("assets/resource\_allocation.png")
else:
st.warning("resource\_allocation.png not found")

# ==========================

# TABLE

# ==========================

st.header("📋 Junction Risk Summary")

risk = pd.read\_csv(
"data/junction\_risk\_summary.csv"
)

st.dataframe(
risk.sort\_values(
"risk\_score",
ascending=False
),
use\_container\_width=True
)

# ==========================

# FUTURE TABLE

# ==========================

st.header("📈 Emerging Hotspots")

future = pd.read\_csv(
"data/future\_hotspot\_predictions.csv"
)

st.dataframe(
future.sort\_values(
"growth\_percent",
ascending=False
),
use\_container\_width=True
)

# ==========================

# MAP

# ==========================

st.header("🗺️ Cluster Analysis Map")

if os.path.exists("maps/cluster\_map.html"):

```
with open(
    "maps/cluster_map.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

st.components.v1.html(
    html,
    height=600,
    scrolling=True
)
```

else:
st.warning("cluster\_map.html not found")
