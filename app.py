import streamlit as st
import pandas as pd
import os

# =====================================

# PAGE CONFIG

# =====================================

st.set_page_config(
page_title="AI Parking Intelligence",
page_icon="🚦",
layout="wide"
)

# =====================================

# LOAD DATA

# =====================================

risk = pd.read_csv(
"data/junction_risk_summary.csv"
)

future = pd.read_csv(
"data/future_hotspot_predictions.csv"
)

# =====================================

# SIDEBAR

# =====================================

st.sidebar.title("🚦 Navigation")

page = st.sidebar.radio(
"Select Module",
[
"Overview",
"Risk Analysis",
"Future Hotspots",
"Resource Allocation",
"Cluster Analysis"
]
)

# =====================================

# OVERVIEW

# =====================================

if page == "Overview":

```
st.title("🚦 AI-Powered Parking Violation Intelligence System")

st.markdown(
    """
    Intelligent Traffic Enforcement & Parking Violation Analytics Platform
    """
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Violations",
    "298,450"
)

col2.metric(
    "Locations",
    "10,942"
)

col3.metric(
    "Junctions",
    "168"
)

col4.metric(
    "Police Stations",
    "54"
)

st.divider()

st.subheader("📌 Executive Summary")

st.info(
    """
    This system analyzes Bengaluru parking violations to identify
    high-risk junctions, predict emerging hotspots, recommend
    enforcement allocation, and support proactive traffic management.
    """
)

st.subheader("⚠️ Top High-Risk Junctions")

st.dataframe(
    risk.sort_values(
        "risk_score",
        ascending=False
    ).head(10),
    use_container_width=True
)
```

# =====================================

# RISK ANALYSIS

# =====================================

elif page == "Risk Analysis":

```
st.title("⚠️ Risk Analysis")

if os.path.exists("assets/top_risk_junctions.png"):
    st.image(
        "assets/top_risk_junctions.png",
        use_container_width=True
    )

if os.path.exists("assets/risk_distribution.png"):
    st.image(
        "assets/risk_distribution.png",
        use_container_width=True
    )

st.subheader("Top Risk Junctions")

st.dataframe(
    risk.sort_values(
        "risk_score",
        ascending=False
    ),
    use_container_width=True
)
```

# =====================================

# FUTURE HOTSPOTS

# =====================================

elif page == "Future Hotspots":

```
st.title("🔮 Future Hotspot Prediction")

if os.path.exists("assets/future_hotspots.png"):
    st.image(
        "assets/future_hotspots.png",
        use_container_width=True
    )

st.subheader("Predicted Emerging Hotspots")

st.dataframe(
    future.sort_values(
        "growth_percent",
        ascending=False
    ),
    use_container_width=True
)
```

# =====================================

# RESOURCE ALLOCATION

# =====================================

elif page == "Resource Allocation":

```
st.title("👮 Resource Allocation Recommendations")

if os.path.exists("assets/resource_allocation.png"):
    st.image(
        "assets/resource_allocation.png",
        use_container_width=True
    )

st.subheader("Recommended Enforcement Strategy")

st.dataframe(
    risk[
        [
            "junction_name",
            "risk_score",
            "risk_level",
            "recommendation"
        ]
    ].sort_values(
        "risk_score",
        ascending=False
    ),
    use_container_width=True
)
```

# =====================================

# CLUSTER ANALYSIS

# =====================================

elif page == "Cluster Analysis":

```
st.title("🗺️ Geographic Cluster Analysis")

if os.path.exists("maps/cluster_map.html"):

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

else:
    st.warning(
        "cluster_map.html not found"
    )

st.info(
    """
    K-Means clustering was used to identify violation concentration
    zones across Bengaluru. These clusters help traffic authorities
    prioritize surveillance and enforcement deployment.
    """
)
```
