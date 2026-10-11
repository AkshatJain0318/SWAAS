import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# --- CONFIG & CSS ---
st.set_page_config(page_title="SWAAS - Premium Air OS", page_icon="🌍", layout="wide")

# Custom Premium Dark Theme CSS
st.markdown("""
<style>
    .main { background-color: #0B0E14; }
    .stMetric { background-color: #151A22; padding: 20px; border-radius: 12px; border-left: 5px solid #00E676; box-shadow: 0px 5px 15px rgba(0,0,0,0.3); }
    .terminal-box { background-color: #050505; color: #00FF41; font-family: 'Courier New', Courier, monospace; padding: 20px; border-radius: 8px; border: 1px solid #1F2937; text-shadow: 0 0 5px #00FF41; }
    h1, h2, h3 { color: #E2E8F0; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3203/3203079.png", width=60)
st.sidebar.title("SWAAS OS")
st.sidebar.caption("Enterprise Edition v2.0")
st.sidebar.divider()

selected_city = st.sidebar.selectbox("📍 Select Region", ["Indore", "Dhar", "Ujjain", "Ratlam", "Dewas"])
sim_mode = st.sidebar.radio("🔥 Threat Simulation", ["Normal Day", "Severe Stubble Burning", "Industrial Smog"])

# --- DYNAMIC DATA ENGINE ---
city_coords = {"Indore": (22.7196, 75.8577), "Dhar": (22.5937, 75.3046), "Ujjain": (23.1793, 75.7849), "Ratlam": (23.3315, 75.0367), "Dewas": (22.9676, 76.0534)}
lat, lon = city_coords[selected_city]

if sim_mode == "Severe Stubble Burning":
    aqi = np.random.randint(380, 480)
    fire_count = np.random.randint(20, 40)
    status_color = "#FF3D00"
elif sim_mode == "Industrial Smog":
    aqi = np.random.randint(220, 310)
    fire_count = np.random.randint(5, 12)
    status_color = "#FF9100"
else:
    aqi = np.random.randint(40, 90)
    fire_count = np.random.randint(0, 3)
    status_color = "#00E676"

indoor_aqi = int(aqi * 0.25) + 10 # Filtered by SWAAS IoT

# --- MAIN UI TABS ---
st.title(f"🌍 SWAAS Intelligence Hub: {selected_city}")
st.markdown("Advanced AI tracking, micro-climate automation, and economic interventions.")

tab1, tab2, tab3 = st.tabs(["📊 Global Dashboard", "⚡ IoT & Logistics Automation", "🌾 Carbon Wallet & Health"])

with tab1:
    st.subheader("Live Environmental Telemetry")
    
    # Premium Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Outdoor AQI", aqi, delta="Critical" if aqi>200 else "Stable", delta_color="inverse")
    c2.metric("Indoor AQI (Filtered)", indoor_aqi, delta="Secured by SWAAS" if aqi>200 else "Normal")
    c3.metric("Active Fire Hotspots", fire_count, delta="High Alert" if fire_count>10 else "Low")
    c4.metric("AI Prediction (Next 24h)", f"{int(aqi*1.15)} Expected", delta="+15% Smog Trend", delta_color="inverse")

    col_gauge, col_map = st.columns([1.2, 2])
    
    with col_gauge:
        # 1. Plotly Speedometer/Gauge Chart
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = aqi,
            title = {'text': "Live Air Toxicity Level", 'font': {'color': "white"}},
            gauge = {
                'axis': {'range': [0, 500], 'tickcolor': "white"},
                'bar': {'color': "rgba(255,255,255,0.8)"},
                'steps': [
                    {'range': [0, 100], 'color': "#00E676"},
                    {'range': [100, 200], 'color': "#FFEA00"},
                    {'range': [200, 300], 'color': "#FF9100"},
                    {'range': [300, 500], 'color': "#FF3D00"}],
            }
        ))
        fig_gauge.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor="rgba(0,0,0,0)", font={'color': "white"})
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_map:
        # 2. Plotly Darkmatter Map
        st.caption("Satellite Stubble Fire Detection (Carto-Darkmatter Engine)")
        df_fires = pd.DataFrame({
            'lat': np.random.normal(lat, 0.08, fire_count),
            'lon': np.random.normal(lon, 0.08, fire_count),
            'intensity': np.random.uniform(60, 100, fire_count)
        })
        if fire_count > 0:
            fig_map = px.scatter_mapbox(df_fires, lat="lat", lon="lon", color="intensity", size="intensity",
                                      color_continuous_scale=px.colors.sequential.YlOrRd, size_max=15, zoom=9,
                                      mapbox_style="carto-darkmatter")
            fig_map.update_layout(height=350, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.success("No active thermal anomalies detected in this sector.")

with tab2:
    st.subheader("School Micro-Climate & Fleet Rerouting")
    col_iot, col_fleet = st.columns(2)
    
    with col_iot:
        # 3. Terminal Style Logs
        st.markdown("**ESP32 IoT Node Console (Live)**")
        if aqi > 200:
            st.markdown('<div class="terminal-box">sys.log > OUTDOOR LIMIT BREACHED<br>sys.log > EXECUTING SWAAS PROTOCOL...<br>hardware > AIR_PURIFIER_RELAY [ENGAGED]<br>hardware > HVAC_INTAKE [ISOLATED]<br>network > Admin notified: Suspend P.E. classes.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="terminal-box">sys.log > AIR QUALITY WITHIN WHO LIMITS<br>hardware > AIR_PURIFIER_RELAY [STANDBY]<br>hardware > HVAC_INTAKE [AUTO-OPEN]<br>network > Monitoring telemetry...</div>', unsafe_allow_html=True)
            
    with col_fleet:
        st.markdown("**AI Fleet Routing System**")
        if aqi > 250:
            st.error("⚠️ Bus routes automatically diverted away from high-density smoke corridors.")
            st.write("🚌 **Route 04 (City Center):** Rerouted via highway (+12m ETA)")
            st.write("🚌 **Route 09 (Outskirts):** Delayed by 30 mins to avoid inversion layer.")
        else:
            st.success("✅ All school fleets running on optimal standard routes.")

with tab3:
    st.subheader("Economic & Health Impact Engine")
    h1, h2 = st.columns(2)
    
    with h1:
        st.markdown("**🌾 Farmer Carbon Wallet**")
        st.write("Incentivizing farmers to sell stubble to biogas plants instead of burning it.")
        acres = st.slider("Farm Size (Acres)", 1, 20, 5)
        tons = acres * 2.5
        st.info(f"💰 **Potential Earnings:** ₹ {tons * 2200:,.0f} (Biomass Sale to Industries)")
        st.success(f"🌱 **Carbon Credits Unlocked:** {tons * 0.4:.1f} Tradable Credits")
        
    with h2:
        st.markdown("**🫁 Real-world Health Impact**")
        hours = st.slider("Hours spent outdoors today", 1, 8, 3)
        cig_eq = round((aqi / 22) * (hours / 24), 1)
        st.markdown(f"### 🚬 Equals smoking **{cig_eq}** cigarettes.")
        if aqi > 200:
            st.warning(f"📲 SMS Alert Gateway: Dispatched automated warnings to 412 registered asthma patients in {selected_city}.")
