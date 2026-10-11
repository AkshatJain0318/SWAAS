import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- PAGE CONFIGURATION & THEME ---
st.set_page_config(page_title="SWAAS - Premium Air Intel OS", page_icon="🌍", layout="wide")

# Extreme Premium Cyber-Glow UI Design using inject CSS
st.markdown("""
<style>
    .main { background-color: #080B10; }
    /* Modern Glassmorphic Dashboard Cards */
    .premium-card {
        background: linear-gradient(145deg, #121824, #0d121c);
        border: 1px solid #233149;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
    }
    .metric-value { font-size: 36px; font-weight: 800; color: #00FFCC; }
    .metric-label { font-size: 14px; color: #8F9CAE; font-weight: 600; text-transform: uppercase; }
    /* Beautiful Custom Logs and Live Terminal */
    .terminal-header { background: #1B2330; padding: 10px 15px; border-radius: 8px 8px 0 0; font-family: monospace; font-size: 12px; color: #8F9CAE; border: 1px solid #2D3A4F; }
    .terminal-body {
        background-color: #05070A;
        color: #39FF14;
        font-family: 'Courier New', Courier, monospace;
        padding: 20px;
        border-radius: 0 0 8px 8px;
        border: 1px solid #2D3A4F;
        border-top: none;
        line-height: 1.6;
        font-size: 14px;
        box-shadow: inset 0 0 10px rgba(0, 255, 20, 0.1);
    }
    /* Danger Alert Callout */
    .alert-banner {
        background: rgba(255, 61, 0, 0.08);
        border: 1px solid #FF3D00;
        border-radius: 10px;
        padding: 15px 20px;
        color: #FFA285;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title & Dashboard Banner
st.title("🌍 SWAAS OS: Enterprise-Grade Air Intelligence Network")
st.markdown("🌐 **Malwa Region Operations Node • Multi-Dimensional Micro-Climate Tracking & Automated Interventions**")
st.divider()

# --- MALWA REGION CONFIGURATOR ---
malwa_data = {
    "Indore": {"lat": 22.7196, "lon": 75.8577, "areas": ["Vijay Nagar", "Palasia", "Rajwada", "Sanwer Road Industrial"]},
    "Dhar": {"lat": 22.5937, "lon": 75.3046, "areas": ["Pithampur (SEZ)", "Dhar City", "Mandu", "Manawar"]},
    "Ujjain": {"lat": 23.1793, "lon": 75.7849, "areas": ["Mahakal Corridor", "Freeganj", "Nagziri", "Makshi Road"]},
    "Ratlam": {"lat": 23.3315, "lon": 75.0367, "areas": ["Station Road", "Jaora", "Sailana"]},
    "Dewas": {"lat": 22.9676, "lon": 76.0534, "areas": ["Bank Note Press", "AB Road", "Industrial Area 1"]}
}

# Sidebar Controls
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3203/3203079.png", width=65)
st.sidebar.markdown("### **🛰️ SWAAS OS Control Panel**")
st.sidebar.caption("Filter data & configure scenario modeling")

selected_city = st.sidebar.selectbox("📍 Select District", list(malwa_data.keys()))
selected_area = st.sidebar.selectbox("🏘️ Select Area/Cluster", malwa_data[selected_city]["areas"])

st.sidebar.divider()
sim_mode = st.sidebar.radio("🔥 Situation Scenario", ["Standard (Normal Day)", "Extreme Stubble Burning", "Heavy Industrial Smog"])

# Dynamic Simulation Logic
base_aqi = 50
if sim_mode == "Extreme Stubble Burning":
    base_aqi = np.random.randint(340, 430)
elif sim_mode == "Heavy Industrial Smog":
    base_aqi = np.random.randint(230, 290)

if "Industrial" in selected_area or "Pithampur" in selected_area or "Sanwer Road" in selected_area:
    outdoor_aqi = base_aqi + np.random.randint(40, 80)
else:
    outdoor_aqi = base_aqi + np.random.randint(-15, 15)

# Calculate system values
indoor_aqi = int(outdoor_aqi * 0.22) + 12
fire_points = 45 if sim_mode == "Extreme Stubble Burning" else (12 if sim_mode == "Heavy Industrial Smog" else 1)

# TABS - PREVIOUS HIGHLY RATED UI WITH HIGHLY PREMIUM ENHANCEMENTS
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 Live Threat Map", 
    "🏫 School Safety IoT", 
    "🫁 Health Index & Alerting", 
    "🌾 Farmer Carbon Wallet",
    "🏛️ Government GRAP & Citizens Portal"
])

# --- TAB 1: LIVE MAP & TELEMETRY ---
with tab1:
    st.markdown(f"### 🛰️ Live Geospatial Analysis • {selected_area}, {selected_city}")
    
    # Telemetry Card Grid
    col_x, col_y, col_z, col_w = st.columns(4)
    with col_x:
        st.markdown(f"""<div class='premium-card'>
            <div class='metric-label'>Outdoor AQI</div>
            <div class='metric-value' style='color: {"#FF3333" if outdoor_aqi > 250 else ("#FF9900" if outdoor_aqi > 120 else "#00FFCC")};'>{outdoor_aqi}</div>
            <div style='color:#8F9CAE; font-size:12px; margin-top:5px;'>✦ Local Spot Level Sensor</div>
        </div>""", unsafe_allow_html=True)
    with col_y:
        st.markdown(f"""<div class='premium-card'>
            <div class='metric-label'>Classroom Indoor AQI</div>
            <div class='metric-value'>{indoor_aqi}</div>
            <div style='color:#00FFCC; font-size:12px; margin-top:5px;'>🛡️ Filtered & Isolated by AI</div>
        </div>""", unsafe_allow_html=True)
    with col_z:
        st.markdown(f"""<div class='premium-card'>
            <div class='metric-label'>Wind Velocity</div>
            <div class='metric-value'>19.5 km/h NW</div>
            <div style='color:#8F9CAE; font-size:12px; margin-top:5px;'>➦ Trajectory direction towards city</div>
        </div>""", unsafe_allow_html=True)
    with col_w:
        st.markdown(f"""<div class='premium-card'>
            <div class='metric-label'>Satellite Anomalies</div>
            <div class='metric-value'>{fire_points} Detected</div>
            <div style='color:{"#FF3333" if fire_points > 15 else "#8F9CAE"}; font-size:12px; margin-top:5px;'>🔥 High-temp hotspots</div>
        </div>""", unsafe_allow_html=True)

    col_map, col_alerts = st.columns([2, 1])
    
    with col_map:
        st.markdown("#### Real-Time Sensor Grid & Fire Hotspots")
        city_lat = malwa_data[selected_city]["lat"]
        city_lon = malwa_data[selected_city]["lon"]
        
        # Streamlit 2D Map - FAST & ROBUST
        map_df = pd.DataFrame({
            'lat': np.random.normal(city_lat, 0.08, fire_points),
            'lon': np.random.normal(city_lon, 0.08, fire_points)
        })
        st.map(map_df, zoom=10, color="#FF1E27" if outdoor_aqi > 180 else "#00FFCC")

    with col_alerts:
        st.markdown("#### Live Network Action Log")
        if outdoor_aqi > 200:
            st.markdown(f"""<div class='alert-banner'>
                ⚡ <strong>AQI SPARK ALERTER:</strong><br>
                Hazardous particulate detection has trigger action. Heavy plumes verified around {selected_city} outskirts. SWAAS protocols on active standby.
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div style='background: rgba(0, 255, 204, 0.05); border: 1px solid #00FFCC; border-radius: 10px; padding: 15px 20px; color: #D1FFFA; margin-bottom: 20px;'>
                🟢 <strong>ENVIRONMENTAL HEALTH GOOD:</strong><br>
                Normal air metrics. Regional filters are idling. No action triggers dispatched.
            </div>""", unsafe_allow_html=True)

        st.markdown("**🔔 Operational Telemetry Stream**")
        st.table(pd.DataFrame({
            "Time": [datetime.now().strftime("%H:%M"), "14:45", "12:12"],
            "Location": [selected_area, "Indore BYPASS", "Pithampur Sec-1"],
            "Event": ["Sensors updated", "Air Plume Spike", "Device ping ok"],
            "Code": ["OK_200", "WARNING_412", "SYSTEM_IDLE"]
        }))

# --- TAB 2: SCHOOL SAFETY IoT ---
with tab2:
    st.markdown("### ⚡ Automated Micro-Climate System (IoT Gateway)")
    st.caption("Closing the airfiltration loop during severe outside pollution days.")
    
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown(f"#### 🏫 Micro-Climate Protocol: {selected_area} Public School")
        if outdoor_aqi > 200:
            st.error("🔴 **OUTDOOR PLUME REACHED THRESHOLD LIMIT**")
            st.markdown("""<div class='terminal-header'>⚙️ LIVE IoT MODULE RESPONSE</div>
            <div class='terminal-body'>
            [CONNECTING TO SWAAS-ESP32 NODE_44]<br>
            > [RELAY 1] Classroom Air Purifiers -> FORCED ON (TURBO MODE)<br>
            > [RELAY 2] Central HVAC Fresh Air Intakes -> ISOLATED (SHUT)<br>
            > [EMAIL] Dispatch Alert to Admin & PE Staff -> COMPLETED<br>
            > [STATUS] Direct Warning: 'Move P.E. sports indoors immediately' -> SENT
            </div>""", unsafe_allow_html=True)
        else:
            st.success("🟢 **MICRO-CLIMATE: NORMAL OPERATIONS**")
            st.markdown("""<div class='terminal-header'>⚙️ LIVE IoT MODULE RESPONSE</div>
            <div class='terminal-body'>
            [SYSTEM STABLE - CONNECTING TO SWAAS-ESP32_NODE_44]<br>
            > [RELAY 1] Classroom Air Purifiers -> STANDBY (ECO)<br>
            > [RELAY 2] Central HVAC Intakes -> NORMAL (OPEN)<br>
            > [STATUS] Monitoring local sensor updates (PM2.5 = Normal)<br>
            > All campus modules running on efficiency schedules.
            </div>""", unsafe_allow_html=True)
            
    with sc2:
        st.markdown("#### 🚌 Dynamic Fleet Route Rerouting")
        st.write("Ensuring kids aren't exposed to excessive inhalation during morning/evening commute.")
        if outdoor_aqi > 250:
            st.warning("⚠️ **TRANSIT EXPOSURE THREAT ACTIVE**")
            st.write(f"- 🚌 **School Bus 04 (Indore bypass -> {selected_city}):** Smog warning. Redirecting via Ring road. (+12 mins ETA)")
            st.write("- 🚌 **Bus 07 (Suburbs):** Shifting to standby. Parents updated via SMS app alert.")
        else:
            st.success("✅ **OPTIMAL ROUTE SCHEDULING ACTIVE**")
            st.write("- All SWAAS-monitored fleet routes on safe optimal routes with 0 expected pollution delays.")

# --- TAB 3: HEALTH INDEX & WARNINGS ---
with tab3:
    st.markdown("### 🫁 Targeted Alerting & Invisible Health Translation")
    
    col_health1, col_health2 = st.columns(2)
    with col_health1:
        st.markdown("#### The Cigarette Equivalent Model")
        st.write("Translating invisible particulate micro-grams into a tangible comparison.")
        hours_active = st.slider("Select hours spent outside today:", 1, 12, 4)
        cig_eq = round((outdoor_aqi / 22) * (hours_active / 24), 1)
        
        st.markdown(f"""<div class='premium-card' style='border-left: 5px solid #FF3D00;'>
            <div class='metric-label' style='color:#FFA285;'>Cigarettes Inhaled Today</div>
            <div class='metric-value' style='color:#FF4500;'>🚬 {cig_eq} Cigarettes</div>
            <div style='color:#8F9CAE; font-size:12px; margin-top:5px;'>
                Exposure to PM2.5 in {selected_area} is equivalent to active smoking.
            </div>
        </div>""", unsafe_allow_html=True)
        
    with col_health2:
        st.markdown(f"#### 💬 Hyper-Local Alert Broadcast • {selected_city}")
        st.write("Unlike traditional broadcast alarms, SWAAS targets based on specific risk lists.")
        
        sms_data = pd.DataFrame({
            "Individual ID": ["PATIENT_A-904", "PATIENT_B-002", "PATIENT_C-452"],
            "Diagnostic / Need": ["Chronic Asthma", "Senior Citizen", "Severe Bronchitis"],
            "Grid Hub Location": [f"{selected_city} Center", selected_area, "Outskirts Grid"],
            "SWAAS Alert Delivery": ["📬 Delivered (SMS)" if outdoor_aqi > 200 else "⏳ Standby"] * 3
        })
        st.table(sms_data)
        if outdoor_aqi > 200:
            st.info("🚨 **Sample Gateway Outgoing Payload**: SWAAS Alert! Stubble smoke spikes detected in your grid zone. If asthmatic/sensitive, please close windows & avoid outdoor activities today.")

# --- TAB 4: FARMER CARBON WALLET ---
with tab4:
    st.markdown("### 🌾 SWAAS Farmer Carbon Wallet")
    st.markdown("Enabling an incentivized stubble-to-wealth alternative instead of penalizing growers.")
    
    f_c1, f_c2 = st.columns([1, 1.2])
    with f_c1:
        st.markdown("#### Calculate Farmer Selling Incentive")
        farm_acres = st.number_input("Enter Field Farm Size (Acres)", min_value=1, value=8)
        biomass_tons = farm_acres * 2.5 # multiplier
        
        b_price = biomass_tons * 2200
        carbon_bonus = biomass_tons * 0.4
        
        st.write("By trading stubble with processing industries instead of burning, the estimated wallet return is:")
        
        st.metric("Potential Additional Income (Biomass)", f"₹ {b_price:,.0f}", f"₹ 2,200 / Ton selling incentive")
        st.metric("Earned Carbon Credits Offset", f"{carbon_bonus:.1f} Credits", "Tradable Credits index")
        
    with f_c2:
        st.markdown("#### 🔄 Biogas & Processing Ecosystem Mapping")
        st.info("By selling unburnt biomass, the local farmer diverts waste to eco-processors.")
        st.write("- **Biomass Procurement Agent:** Linked with Malwa regional centers (Indore, Dhar).")
        st.write(f"- **Unlocking carbon credits:** Estimated {carbon_bonus:.1f} carbon credits generated automatically based on SWAAS verification.")
        
        st.markdown("""<div style='background: rgba(57, 255, 20, 0.05); border: 1px solid #39FF14; border-radius: 10px; padding: 15px 20px;'>
            <strong>Impact:</strong> Diverting this stubble prevents tons of Co2, NOx, and Carbon particulate release into the city airflow. Only verifiably clean stubble offsets can generate carbon portfolio balances.
        </div>""", unsafe_allow_html=True)

# --- TAB 5: GOVT & CITIZENS GATEWAY ---
with tab5:
    st.markdown("### 🏛️ Municipal GRAP Interface & Citizens Incident Report Grid")
    
    g_col1, g_col2 = st.columns([1.2, 1])
    with g_col1:
        st.markdown(f"#### Government Action Plan Trigger Protocol ({selected_city})")
        st.caption("Active administrative rules on critical heavy impact AQI spikes.")
        
        if outdoor_aqi > 300:
            st.error("🔴 **STAGE 4 ACTIVATED: Severe Air Inversion**")
            st.checkbox("Forced Ban on open industrial emissions & generators", value=True, disabled=True)
            st.checkbox("Emergency suspension of all major outdoor construction", value=True, disabled=True)
            st.checkbox("Banning heavy commercial trucks from core city zones", value=True, disabled=True)
        elif outdoor_aqi > 200:
            st.warning("⚠️ **STAGE 2 ACTIVATED: Moderate/Poor Smoke Spikes**")
            st.checkbox("Mandatory ban on coal burners / tandoor fires", value=True, disabled=True)
            st.checkbox("Active automated water-sprinklers on unpaved roads", value=True, disabled=True)
        else:
            st.success("🟢 **STANDARD NORMAL: NO SPECIAL BANS TRIGGERED**")
            st.write("Environmental indexes are verified safe. Regular regional guidelines applicable.")
            
    with g_col2:
        st.markdown("#### 📸 Community Active Incident Reporting")
        st.write("Give normal citizens an app tool to pinpoint illegal burns & trash smoke in real-time.")
        
        with st.form("c_citizen_form"):
            st.selectbox("Incedent Burn Alert", ["Trash/Waste Burning", "Farm Fire (Stubble)", "Excessive Industrial exhaust", "Severe Construction Dust"])
            st.text_area("Specific Incident Location Details:")
            st.file_uploader("Evidence Photo Upload:")
            
            sub = st.form_submit_button("Submit Incident Payload to Gov Node")
            if sub:
                st.success("Alert received! Dispatched alert to Municipal verification team. Tracking Incident ID #SWAAS-0943.")
