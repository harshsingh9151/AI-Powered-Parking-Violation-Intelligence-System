import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="AI Parking Intelligence",
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

if os.path.exists("assets/top_risk_junctions.png"):
    st.image("assets/top_risk_junctions.png")
else:
    st.warning("top_risk_junctions.png not found")

# ==========================
# FUTURE HOTSPOTS
# ==========================

st.header("🔮 Future Hotspot Prediction")

if os.path.exists("assets/future_hotspots.png"):
    st.image("assets/future_hotspots.png")
else:
    st.warning("future_hotspots.png not found")

# ==========================
# RISK DISTRIBUTION
# ==========================

st.header("📊 Risk Distribution")

if os.path.exists("assets/risk_distribution.png"):
    st.image("assets/risk_distribution.png")
else:
    st.warning("risk_distribution.png not found")

# ==========================
# RESOURCE ALLOCATION
# ==========================

st.header("👮 Recommended Enforcement Allocation")

if os.path.exists("assets/resource_allocation.png"):
    st.image("assets/resource_allocation.png")
else:
    st.warning("resource_allocation.png not found")

# ==========================
# TABLE
# ==========================

st.header("📋 Junction Risk Summary")

risk = pd.read_csv(
    "data/junction_risk_summary.csv"
)

st.dataframe(
    risk.sort_values(
        "risk_score",
        ascending=False
    ),
    use_container_width=True
)

# ==========================
# FUTURE TABLE
# ==========================

st.header("📈 Emerging Hotspots")

future = pd.read_csv(
    "data/future_hotspot_predictions.csv"
)

st.dataframe(
    future.sort_values(
        "growth_percent",
        ascending=False
    ),
    use_container_width=True
)

# ==========================
# MAP
# ==========================

st.header("🗺️ Cluster Analysis Map")

if os.path.exists("maps/cluster_map.html"):

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

else:
    st.warning("cluster_map.html not found")
