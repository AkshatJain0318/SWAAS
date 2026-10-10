import streamlit as st
import pandas as pd
import numpy as np
import time

# Page configuration
st.set_page_config(page_title="SWAAS - Malwa Air Intelligence", page_icon="🌬️", layout="wide")

# Custom UI Styling
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1c1f26; padding: 15px; border-radius: 8px; border-left: 4px solid #00ffcc; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .big-font { font-size: 22px !important; font-weight: bold; color: #ff4b4b; }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🌬️ SWAAS: Enterprise Air Intelligence (Malwa Region)")
st.markdown("**Unified Ecosystem for Tracking, School Automation, Public Health & Farmer Incentives**")
st.divider()

# --- MALWA REGION DICTIONARY ---
malwa_data = {
    "Indore": {"lat": 22.7196, "lon": 75.8577, "areas": ["Vijay Nagar", "Palasia", "Rajwada", "Sanwer Road Industrial"]},
    "Dhar": {"lat": 22.5937, "lon": 75.3046, "areas": ["Pithampur (SEZ)", "Dhar City", "Mandu", "Manawar"]},
    "Ujjain": {"lat": 23.1793, "lon": 75.7849, "areas": ["Mahakal Corridor", "Freeganj", "Nagziri", "Makshi Road"]},
    "Ratlam": {"lat": 23.3315, "lon": 75.0367, "areas": ["Station Road", "Jaora", "Sailana"]},
    "Dewas": {"lat": 22.9676, "lon": 76.0534, "areas": ["Bank Note Press", "AB Road", "Industrial Area 1"]}
}

# Sidebar - Location & Scenario Controls
st.sidebar.header("🎛️ Command Center")
st.sidebar.caption("Filter data across the Malwa Region")

selected_city = st.sidebar.selectbox("📍 Select City / District", list(malwa_data.keys()))
selected_area = st.sidebar.selectbox("🏘️ Select Specific Area", malwa_data[selected_city]["areas"])

st.sidebar.divider()
sim_mode = st.sidebar.radio("🔥 Simulation Mode", ["Normal Day", "Stubble Burning Spike", "Industrial Smog Alert"])

# Dynamic Variable Generation based on Scenario & City
base_aqi = 60
if sim_mode == "Stubble Burning Spike":
    base_aqi = np.random.randint(350, 480)
elif sim_mode == "Industrial Smog Alert":
    base_aqi = np.random.randint(220, 310)

# Add minor variations based on area (Industrial areas get slightly higher AQI)
if "Industrial" in selected_area or "Pithampur" in selected_area:
    outdoor_aqi = base_aqi + np.random.randint(30, 70)
else:
    outdoor_aqi = base_aqi + np.random.randint(-20, 20)

indoor_aqi = int(outdoor_aqi * 0.3) + 15  # Assuming PRANA IoT purifiers are running
fire_points = 35 if sim_mode == "Stubble Burning Spike" else (10 if sim_mode == "Industrial Smog Alert" else 2)

# --- REVERTED TO TABS UI ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 Live Map & Intelligence", 
    "🏫 IoT & School Safety", 
    "🫁 Health Impact", 
    "🌾 Farmer Carbon Wallet (NEW)",
    "🏛️ Govt GRAP & Citizen App"
])

with tab1:
    st.subheader(f"🛰️ Live Regional Threat Map: {selected_area}, {selected_city}")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(f"Outdoor AQI ({selected_area})", outdoor_aqi, delta="Hazardous" if outdoor_aqi > 200 else "Stable", delta_color="inverse")
    c2.metric("Filtered Indoor AQI", indoor_aqi, delta="Protected by PRANA" if outdoor_aqi > 200 else "Normal")
    c3.metric("Wind Trajectory", "18 km/h NW", delta="Plume Moving" if outdoor_aqi > 200 else "Clear")
    c4.metric("Active Anomalies", fire_points, delta="High Alert" if fire_points > 10 else "Low")

    # Dynamic Map Generation around the selected city
    city_lat = malwa_data[selected_city]["lat"]
    city_lon = malwa_data[selected_city]["lon"]
    
    st.caption(f"Showing localized satellite data for {selected_city} district...")
    map_data = pd.DataFrame({
        'lat': np.random.normal(city_lat, 0.08, fire_points),
        'lon': np.random.normal(city_lon, 0.08, fire_points)
    })
    st.map(map_data, zoom=10, color="#ff0000" if outdoor_aqi > 200 else "#00ffcc")

with tab2:
    st.subheader("⚡ Automated School Protocol & Fleet Rerouting")
    
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown(f"### 🏫 {selected_area} Public School IoT")
        if outdoor_aqi > 200:
            st.error("🔴 **OUTDOOR THREAT DETECTED**")
            st.code("""
[PRANA IoT GATEWAY - AUTOMATED RESPONSE]
> Smart Plugs: AIR PURIFIERS [TURBO MODE]
> HVAC Intake: [ISOLATED/CLOSED]
> Admin Alert: P.E. Classes Cancelled [EMAIL SENT]
            """, language="yaml")
        else:
            st.success("🟢 **SYSTEM NORMAL**")
            st.code("Purifiers: [STANDBY]\nVentilation: [FRESH AIR MODE]", language="yaml")
            
    with sc2:
        st.markdown("### 🚌 Smart Bus Rerouting")
        if outdoor_aqi > 250:
            st.warning(f"⚠️ Route adjustment active for {selected_city} fleets.")
            st.write("- **Bus Route 4:** Diverted away from heavy smoke zone.")
            st.write("- **ETA Impact:** +12 Minutes")
        else:
            st.info("✅ All fleets operating on optimal routes.")

with tab3:
    st.subheader("🫁 The Cigarette Equivalent & Targeted SMS")
    h_col1, h_col2 = st.columns(2)
    
    with h_col1:
        st.markdown("Translating invisible PM2.5 into understandable health impact.")
        hours_outside = st.slider("Hours spent outside today:", 1, 12, 4)
        cig_equivalent = round((outdoor_aqi / 22) * (hours_outside / 24), 1)
        
        st.markdown(f"<p class='big-font'>Breathing air in {selected_area} for {hours_outside} hours today equals smoking {cig_equivalent} cigarettes.</p>", unsafe_allow_html=True)
        
    with h_col2:
        st.markdown(f"**SMS Alert Gateway ({selected_city} Vulnerable DB)**")
        st.write("Alerts dispatched only to registered asthma/elderly patients in the plume's path.")
        sms_df = pd.DataFrame({
            "User ID": ["USR-992", "USR-104", "USR-442"],
            "Condition": ["Asthma", "Senior Citizen", "Bronchitis"],
            "Location": [f"{selected_city} Central", selected_area, "Outskirts"],
            "Alert Sent?": ["✅ Dispatched" if outdoor_aqi > 200 else "⏳ Standby"] * 3
        })
        st.table(sms_df)

with tab4:
    st.subheader("🌾 Farmer Carbon Wallet (Stubble-to-Wealth)")
    st.markdown("Instead of fining farmers, SWAAS calculates their potential earnings if they sell stubble to Bio-Gas/Cardboard plants instead of burning it.")
    
    farm_acres = st.number_input("Enter Farm Size (Acres)", min_value=1, value=10)
    stubble_tons = farm_acres * 2.5 # Approx 2.5 tons per acre
    
    f1, f2, f3 = st.columns(3)
    f1.metric("Total Stubble Generated", f"{stubble_tons} Tons")
    f2.metric("Bio-Mass Selling Price", f"₹ {stubble_tons * 2000:,}", "₹2000/ton")
    f3.metric("Carbon Credits Earned", f"{round(stubble_tons * 0.4, 1)} Credits", "Tradeable asset")
    
    st.success(f"🌱 By not burning, this farmer in {selected_city} can earn an additional **₹ {stubble_tons * 2000:,}** and prevent **{round(stubble_tons * 1.5, 1)} tons** of CO2 emissions!")

with tab5:
    st.subheader("🏛️ Govt. GRAP Center & Citizen Reports")
    
    g1, g2 = st.columns([1.5, 1])
    with g1:
        st.markdown(f"**Graded Response Action Plan (GRAP) - {selected_city}**")
        if outdoor_aqi > 400:
            st.error("🔥 **STAGE 4: SEVERE PLUS** (Automated Legal Bans Triggered)")
            st.checkbox("Ban on all construction activities", value=True, disabled=True)
            st.checkbox("Heavy diesel trucks banned", value=True, disabled=True)
            st.checkbox("Schools shifted to online", value=True, disabled=True)
        elif outdoor_aqi > 250:
            st.warning("⚠️ **STAGE 2: VERY POOR**")
            st.checkbox("Ban on coal/firewood tandoors", value=True, disabled=True)
            st.checkbox("Increase parking fees", value=True, disabled=True)
        else:
            st.success("✅ **STAGE 0: NORMAL** - No emergency restrictions.")
            
    with g2:
        st.markdown("**📸 Live Citizen Reports**")
        st.info(f"📍 **{selected_area}**: Illegal garbage burning reported (12 mins ago) - Ticket #441")
        st.info(f"📍 **{selected_city} Outskirts**: Excessive factory smoke - Ticket #438")
