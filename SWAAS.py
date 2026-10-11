import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="SWAAS - Premium Air Intel OS", page_icon="🌍", layout="wide")

# --- SIDEBAR: TOGGLES (Language & Theme) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3203/3203079.png", width=65)

col_lang, col_theme = st.sidebar.columns(2)
with col_lang:
    language = st.radio("🌐 Language", ["English", "Hindi"])
with col_theme:
    theme = st.radio("🌗 Theme", ["Dark", "Light"])

st.sidebar.divider()

# --- SAFE CSS INJECTION (Fixes Sidebar & Text Colors) ---
if theme == "Dark":
    bg_color = "#080B10"
    sidebar_bg = "#111827"
    card_bg = "linear-gradient(145deg, #121824, #0d121c)"
    border_color = "#233149"
    text_main = "#FFFFFF"
    text_sub = "#8F9CAE"
    terminal_bg = "#05070A"
    alert_bg = "rgba(255, 61, 0, 0.08)"
else:
    bg_color = "#F4F7F6"
    sidebar_bg = "#FFFFFF"
    card_bg = "white"
    border_color = "#E2E8F0"
    text_main = "#1E293B"
    text_sub = "#64748B"
    terminal_bg = "#F8FAFC"
    alert_bg = "rgba(255, 61, 0, 0.05)"

st.markdown(f"""
<style>
    /* Global Backgrounds */
    .stApp {{ background-color: {bg_color}; }}
    [data-testid="stSidebar"] {{ background-color: {sidebar_bg} !important; border-right: 1px solid {border_color}; }}
    [data-testid="stHeader"] {{ background-color: transparent !important; }}
    
    /* Fix Text Colors Everywhere */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stRadio, .stSelectbox, .stCheckbox span {{ color: {text_main} !important; }}
    
    /* Premium Cards */
    .premium-card {{
        background: {card_bg};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.1);
    }}
    .metric-value {{ font-size: 36px; font-weight: 800; }}
    .metric-label {{ font-size: 14px; color: {text_sub}; font-weight: 600; text-transform: uppercase; }}
    
    /* Terminal Styles */
    .terminal-header {{ background: {border_color}; padding: 10px 15px; border-radius: 8px 8px 0 0; font-family: monospace; font-size: 12px; color: {text_main}; font-weight: bold; }}
    .terminal-body {{
        background-color: {terminal_bg};
        color: #00A676;
        font-family: 'Courier New', Courier, monospace;
        padding: 20px;
        border-radius: 0 0 8px 8px;
        border: 1px solid {border_color};
        border-top: none;
        line-height: 1.6;
        font-size: 14px;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
    }}
    
    /* Alert Banners */
    .alert-banner {{
        background: {alert_bg};
        border: 1px solid #FF3D00;
        border-radius: 10px;
        padding: 15px 20px;
        color: {text_main};
        margin-bottom: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# --- UI HEADER ---
if language == "English":
    st.title("🌍 SWAAS OS: Enterprise-Grade Air Intelligence Network")
    st.markdown("**🌐 Malwa Region Operations Node • Multi-Dimensional Micro-Climate Tracking & Automated Interventions**")
else:
    st.title("🌍 SWAAS OS: एंटरप्राइज एयर इंटेलिजेंस नेटवर्क")
    st.markdown("**🌐 मालवा रीजन नोड • वायु गुणवत्ता ट्रैकिंग और ऑटोमेशन**")
st.divider()

# --- MALWA REGION CONFIGURATOR ---
malwa_data = {
    "Indore": {"lat": 22.7196, "lon": 75.8577, "areas": ["Vijay Nagar", "Palasia", "Rajwada", "Sanwer Road Industrial"]},
    "Dhar": {"lat": 22.5937, "lon": 75.3046, "areas": ["Pithampur (SEZ)", "Dhar City", "Mandu", "Manawar"]},
    "Ujjain": {"lat": 23.1793, "lon": 75.7849, "areas": ["Mahakal Corridor", "Freeganj", "Nagziri", "Makshi Road"]},
    "Ratlam": {"lat": 23.3315, "lon": 75.0367, "areas": ["Station Road", "Jaora", "Sailana"]},
    "Dewas": {"lat": 22.9676, "lon": 76.0534, "areas": ["Bank Note Press", "AB Road", "Industrial Area 1"]}
}

st.sidebar.markdown("### **🛰️ SWAAS OS Control Panel**" if language == "English" else "### **🛰️ कंट्रोल पैनल**")
st.sidebar.caption("Filter data & configure scenario modeling" if language == "English" else "डेटा फ़िल्टर करें और स्थिति सेट करें")

selected_city = st.sidebar.selectbox("📍 Select District" if language == "English" else "📍 जिला चुनें", list(malwa_data.keys()))
selected_area = st.sidebar.selectbox("🏘️ Select Area/Cluster" if language == "English" else "🏘️ क्षेत्र / क्लस्टर चुनें", malwa_data[selected_city]["areas"])
st.sidebar.divider()

sim_options = ["Standard (Normal Day)", "Extreme Stubble Burning", "Heavy Industrial Smog"] if language == "English" else ["सामान्य दिन", "पराली जलने का आपातकाल", "भारी औद्योगिक धुआं"]
sim_mode = st.sidebar.radio("🔥 Situation Scenario" if language == "English" else "🔥 स्थिति (Scenario)", sim_options)

# --- DYNAMIC SIMULATION LOGIC ---
base_aqi = 50
if sim_mode == sim_options[1]: # Extreme Stubble Burning
    base_aqi = np.random.randint(340, 430)
elif sim_mode == sim_options[2]: # Industrial Smog
    base_aqi = np.random.randint(230, 290)

if "Industrial" in selected_area or "Pithampur" in selected_area or "Sanwer Road" in selected_area:
    outdoor_aqi = base_aqi + np.random.randint(40, 80)
else:
    outdoor_aqi = base_aqi + np.random.randint(-15, 15)

indoor_aqi = int(outdoor_aqi * 0.22) + 12
fire_points = 45 if sim_mode == sim_options[1] else (12 if sim_mode == sim_options[2] else 1)
color_aqi = "#FF3333" if outdoor_aqi > 250 else ("#FF9900" if outdoor_aqi > 120 else "#00FFCC")

# --- TABS ---
t_tabs = ["🌍 Live Threat Map", "🏫 School Safety IoT", "🫁 Health Index & Alerting", "🌾 Farmer Carbon Wallet", "🏛️ Government GRAP & Citizens Portal"] if language == "English" else ["🌍 लाइव थ्रेट मैप", "🏫 स्कूल सेफ्टी IoT", "🫁 हेल्थ अलर्ट", "🌾 किसान कार्बन वॉलेट", "🏛️ सरकारी GRAP और रिपोर्टिंग पोर्टल"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(t_tabs)

# --- TAB 1: LIVE MAP ---
with tab1:
    col_x, col_y, col_z, col_w = st.columns(4)
    with col_x:
        st.markdown(f"""<div class='premium-card'><div class='metric-label'>{'Outdoor AQI' if language=='English' else 'बाहरी AQI'}</div>
            <div class='metric-value' style='color: {color_aqi};'>{outdoor_aqi}</div>
            <div style='color:{text_sub}; font-size:12px; margin-top:5px;'>✦ Local Spot Sensor</div></div>""", unsafe_allow_html=True)
    with col_y:
        st.markdown(f"""<div class='premium-card'><div class='metric-label'>{'Classroom Indoor AQI' if language=='English' else 'क्लासरूम अंदर का AQI'}</div>
            <div class='metric-value' style='color:#00FFCC;'>{indoor_aqi}</div>
            <div style='color:{text_sub}; font-size:12px; margin-top:5px;'>🛡️ Filtered & Isolated by AI</div></div>""", unsafe_allow_html=True)
    with col_z:
        st.markdown(f"""<div class='premium-card'><div class='metric-label'>{'Wind Velocity' if language=='English' else 'हवा की गति'}</div>
            <div class='metric-value' style='color:#00FFCC;'>19.5 km/h</div>
            <div style='color:{text_sub}; font-size:12px; margin-top:5px;'>➦ Trajectory NW towards city</div></div>""", unsafe_allow_html=True)
    with col_w:
        st.markdown(f"""<div class='premium-card'><div class='metric-label'>{'Satellite Anomalies' if language=='English' else 'सैटेलाइट हॉटस्पॉट'}</div>
            <div class='metric-value' style='color:{"#FF3333" if fire_points > 15 else "#00FFCC"};'>{fire_points}</div>
            <div style='color:{text_sub}; font-size:12px; margin-top:5px;'>🔥 High-temp hotspots</div></div>""", unsafe_allow_html=True)

    col_map, col_alerts = st.columns([2, 1])
    with col_map:
        st.markdown(f"#### {'Real-Time Sensor Grid & Fire Hotspots' if language=='English' else 'रियल-टाइम सेंसर ग्रिड'}")
        
        # EXACT SAME NATIVE MAP
        city_lat = malwa_data[selected_city]["lat"]
        city_lon = malwa_data[selected_city]["lon"]
        map_df = pd.DataFrame({
            'lat': np.random.normal(city_lat, 0.08, fire_points),
            'lon': np.random.normal(city_lon, 0.08, fire_points)
        })
        st.map(map_df, zoom=10, color="#FF1E27" if outdoor_aqi > 180 else "#00FFCC")

    with col_alerts:
        st.markdown(f"#### {'Live Network Action Log' if language=='English' else 'नेटवर्क एक्शन लॉग'}")
        if outdoor_aqi > 200:
            msg = f"Hazardous particulate detection has triggered action. Heavy plumes verified around {selected_city} outskirts. SWAAS protocols on active standby." if language=="English" else f"खतरनाक धुंआ डिटेक्ट हुआ है। {selected_city} के आस-पास SWAAS प्रोटोकॉल एक्टिव कर दिए गए हैं।"
            st.markdown(f"<div class='alert-banner'>⚡ <strong>AQI SPARK ALERTER:</strong><br>{msg}</div>", unsafe_allow_html=True)
        else:
            msg = "Normal air metrics. Regional filters are idling. No action triggers dispatched." if language=="English" else "वायु गुणवत्ता सामान्य है। कोई एक्शन ट्रिगर नहीं हुआ है।"
            st.markdown(f"<div class='alert-banner' style='border-color:#00FFCC; background:rgba(0,255,204,0.05); color:#00FFCC;'>🟢 <strong>ENVIRONMENTAL HEALTH GOOD:</strong><br>{msg}</div>", unsafe_allow_html=True)

        st.markdown(f"**🔔 {'Operational Telemetry Stream' if language=='English' else 'सिस्टम ऑपरेशन्स'}**")
        st.table(pd.DataFrame({
            "Time": [datetime.now().strftime("%H:%M"), "14:45", "12:12"],
            "Location": [selected_area, f"{selected_city} BYPASS", "Pithampur Sec-1"],
            "Event": ["Sensors updated", "Air Plume Spike", "Device ping ok"],
            "Code": ["OK_200", "WARNING_412", "SYSTEM_IDLE"]
        }))

# --- TAB 2: SCHOOL SAFETY ---
with tab2:
    st.markdown("### ⚡ Automated Micro-Climate System (IoT Gateway)" if language == "English" else "### ⚡ ऑटोमेटेड माइक्रो-क्लाइमेट सिस्टम (IoT)")
    st.caption("Closing the airfiltration loop during severe outside pollution days." if language == "English" else "प्रदूषण के दिनों में स्कूलों को सुरक्षित करना।")
    
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown(f"#### 🏫 {'School Protocol' if language=='English' else 'स्कूल सुरक्षा प्रोटोकॉल'}: {selected_area}")
        if outdoor_aqi > 200:
            st.error("🔴 OUTDOOR PLUME REACHED THRESHOLD LIMIT" if language=="English" else "🔴 बाहरी खतरा - सीमा पार")
            terminal_txt = "> [RELAY 1] Classroom Air Purifiers -> FORCED ON (TURBO)\n> [RELAY 2] Central HVAC Intakes -> ISOLATED (SHUT)\n> [EMAIL] Dispatch Alert to Admin & PE Staff -> COMPLETED\n> [STATUS] Direct Warning: 'Move P.E. sports indoors immediately' -> SENT"
            st.markdown(f"<div class='terminal-header'>⚙️ LIVE IoT MODULE RESPONSE</div><div class='terminal-body'>{terminal_txt.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
        else:
            st.success("🟢 MICRO-CLIMATE: NORMAL OPERATIONS" if language=="English" else "🟢 वायु गुणवत्ता सुरक्षित है")
            terminal_txt = "> [RELAY 1] Classroom Air Purifiers -> STANDBY (ECO)\n> [RELAY 2] Central HVAC Intakes -> NORMAL (OPEN)\n> [STATUS] Monitoring local sensor updates (PM2.5 = Normal)\n> All campus modules running on efficiency schedules."
            st.markdown(f"<div class='terminal-header'>⚙️ LIVE IoT MODULE RESPONSE</div><div class='terminal-body'>{terminal_txt.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
            
    with sc2:
        st.markdown(f"#### 🚌 {'Dynamic Fleet Route Rerouting' if language=='English' else 'स्मार्ट स्कूल बस रूटिंग'}")
        st.write("Ensuring kids aren't exposed to excessive inhalation during commute." if language == "English" else "स्कूली बच्चों को जहरीले धुएं से बचाना।")
        if outdoor_aqi > 250:
            st.warning("⚠️ Transit Exposure Threat Active" if language=="English" else "⚠️ बस रूट बदला गया है")
            st.write(f"- 🚌 **Bus 04 ({selected_city} bypass):** Redirecting via Ring road. (+12 mins ETA)")
            st.write(f"- 🚌 **Bus 07 (Suburbs):** Shifting to standby. Parents updated via SMS app alert.")
        else:
            st.success("✅ Optimal Route Scheduling Active" if language=="English" else "✅ बसें सामान्य रूट पर हैं")
            st.write("- All SWAAS-monitored fleet routes on safe optimal routes with 0 expected pollution delays.")

# --- TAB 3: HEALTH ---
with tab3:
    st.markdown("### 🫁 Targeted Alerting & Invisible Health Translation" if language == "English" else "### 🫁 हेल्थ इंडेक्स और अलर्ट सिस्टम")
    col_health1, col_health2 = st.columns(2)
    with col_health1:
        st.markdown(f"#### {'The Cigarette Equivalent Model' if language=='English' else 'सिगरेट के बराबर वायु प्रदूषण'}")
        st.write("Translating invisible particulate micro-grams into a tangible comparison." if language == "English" else "AQI को सिगरेट के धुएं से तुलना करना।")
        hours_active = st.slider("Select hours spent outside today:" if language == "English" else "आज आप कितनी देर बाहर रहे (घंटे):", 1, 12, 4)
        cig_eq = round((outdoor_aqi / 22) * (hours_active / 24), 1)
        st.markdown(f"""<div class='premium-card' style='border-left: 5px solid #FF3D00;'>
            <div class='metric-label' style='color:#FF9900;'>{'Cigarettes Inhaled Today' if language=='English' else 'आज इतनी सिगरेट के बराबर धुआं लिया'}</div>
            <div class='metric-value' style='color:#FF4500;'>🚬 {cig_eq} {'Cigarettes' if language=='English' else 'सिगरेट'}</div>
            <div style='color:{text_sub}; font-size:12px; margin-top:5px;'>Exposure to PM2.5 in {selected_area} is equivalent to active smoking.</div>
        </div>""", unsafe_allow_html=True)
        
    with col_health2:
        st.markdown(f"#### 💬 {'Hyper-Local Alert Broadcast' if language=='English' else 'स्थानीय SMS अलर्ट'}")
        st.write("Unlike traditional alarms, SWAAS targets based on specific risk lists." if language == "English" else "SWAAS सिर्फ रिस्क वाले मरीजों को अलर्ट भेजता है।")
        sms_data = pd.DataFrame({
            "Individual ID": ["PATIENT_A-904", "PATIENT_B-002", "PATIENT_C-452"],
            "Diagnostic / Need": ["Chronic Asthma", "Senior Citizen", "Severe Bronchitis"],
            "Location": [f"{selected_city} Center", selected_area, "Outskirts Grid"],
            "SWAAS Alert Delivery": ["📬 Delivered (SMS)" if outdoor_aqi > 200 else "⏳ Standby"] * 3
        })
        st.table(sms_data)
        
        # MISSING FEATURE 1 RESTORED: TWILIO MOCK PAYLOAD
        if outdoor_aqi > 200:
            payload_msg = "🚨 **Sample Gateway Outgoing Payload**: SWAAS Alert! Stubble smoke spikes detected in your grid zone. If asthmatic/sensitive, please close windows & avoid outdoor activities today." if language == "English" else "🚨 **SMS पेलोड (मरीज के लिए)**: SWAAS अलर्ट! आपके इलाके में धुंआ बढ़ गया है। अस्थमा के मरीज कृपया घर के अंदर रहें और खिड़कियां बंद कर लें।"
            st.info(payload_msg)

# --- TAB 4: FARMER WALLET ---
with tab4:
    st.markdown("### 🌾 SWAAS Farmer Carbon Wallet" if language == "English" else "### 🌾 किसान कार्बन वॉलेट")
    st.markdown("Enabling an incentivized stubble-to-wealth alternative instead of penalizing growers." if language == "English" else "पराली जलाने पर जुर्माना लगाने की बजाय कमाई का मौका देना।")
    
    f_c1, f_c2 = st.columns([1, 1.2])
    with f_c1:
        st.markdown(f"#### {'Calculate Farmer Selling Incentive' if language=='English' else 'किसान की अतिरिक्त आय कैलकुलेट करें'}")
        farm_acres = st.number_input("Enter Field Farm Size (Acres)" if language == "English" else "खेत का आकार (एकड़) दर्ज करें:", min_value=1, value=8)
        biomass_tons = farm_acres * 2.5
        
        b_price = biomass_tons * 2200
        carbon_bonus = biomass_tons * 0.4
        st.write("By trading stubble with processing industries instead of burning, the estimated wallet return is:" if language == "English" else "पराली को जलाने की बजाय उद्योग को बेचने से होने वाली कमाई:")
        
        st.metric("Potential Additional Income (Biomass)", f"₹ {b_price:,.0f}", f"₹ 2,200 / Ton {'selling incentive' if language=='English' else 'बिक्री प्रोत्साहन'}")
        st.metric("Earned Carbon Credits Offset", f"{carbon_bonus:.1f} Credits", "Tradable Credits index" if language == "English" else "ट्रेडेबल क्रेडिट्स")
        
    with f_c2:
        # MISSING FEATURE 2 RESTORED: BIOGAS ECOSYSTEM MAPPING
        st.markdown(f"#### 🔄 {'Biogas & Processing Ecosystem Mapping' if language=='English' else 'बायो-गैस प्रोसेसिंग इकोसिस्टम'}")
        st.info("By selling unburnt biomass, the local farmer diverts waste to eco-processors." if language == "English" else "पराली को जलाने की बजाय बायो-गैस प्लांट को बेचकर इकोसिस्टम को सपोर्ट करें।")
        if language == "English":
            st.write(f"- **Biomass Procurement Agent:** Linked with Malwa regional centers ({selected_city}).")
            st.write(f"- **Unlocking carbon credits:** Estimated {carbon_bonus:.1f} carbon credits generated automatically based on SWAAS verification.")
            st.markdown(f"""<div style='background: {alert_bg}; border: 1px solid #00FFCC; border-radius: 10px; padding: 15px 20px; color:{text_main};'>
                <strong>Impact:</strong> Diverting this stubble prevents tons of Co2, NOx, and Carbon particulate release into the city airflow. Only verifiably clean stubble offsets can generate carbon portfolio balances.
            </div>""", unsafe_allow_html=True)
        else:
            st.write(f"- **बायोमास एजेंट:** {selected_city} रीजनल सेंटर से जुड़ा हुआ।")
            st.write(f"- **कार्बन क्रेडिट्स:** SWAAS वेरिफिकेशन से लगभग {carbon_bonus:.1f} कार्बन क्रेडिट्स जेनरेट हुए।")
            st.markdown(f"""<div style='background: {alert_bg}; border: 1px solid #00FFCC; border-radius: 10px; padding: 15px 20px; color:{text_main};'>
                <strong>प्रभाव:</strong> इस पराली को डाइवर्ट करने से हवा में Co2 और जहरीले धुएं को फैलने से रोका जाता है।
            </div>""", unsafe_allow_html=True)

# --- TAB 5: GRAP & CITIZEN PORTAL ---
with tab5:
    st.markdown("### 🏛️ Municipal GRAP Interface & Citizens Incident Report Grid" if language == "English" else "### 🏛️ सरकारी GRAP नियम और नागरिक रिपोर्ट पोर्टल")
    g_col1, g_col2 = st.columns([1.2, 1])
    
    with g_col1:
        st.markdown(f"#### {'Government Action Plan Trigger Protocol' if language=='English' else 'सरकारी नियम ट्रिगर'}: ({selected_city})")
        st.caption("Active administrative rules on critical heavy impact AQI spikes." if language == "English" else "खराब हवा होने पर ऑटोमैटिक नियम लागू।")
        
        if outdoor_aqi > 300:
            st.error("🔴 STAGE 4 ACTIVATED: Severe Air Inversion" if language == "English" else "🔴 स्टेज 4 लागू: गंभीर स्थिति")
            st.checkbox("Forced Ban on open industrial emissions & generators" if language == "English" else "औद्योगिक उत्सर्जन और जेनरेटर पर प्रतिबंध", value=True, disabled=True)
            st.checkbox("Emergency suspension of all major outdoor construction" if language == "English" else "सभी बड़े आउटडोर निर्माण कार्यों पर रोक", value=True, disabled=True)
            st.checkbox("Banning heavy commercial trucks from core city zones" if language == "English" else "शहर के अंदर ट्रकों की एंट्री पर रोक", value=True, disabled=True)
        elif outdoor_aqi > 200:
            st.warning("⚠️ STAGE 2 ACTIVATED: Moderate/Poor Smoke Spikes" if language == "English" else "⚠️ स्टेज 2 लागू: मध्यम/खराब स्थिति")
            st.checkbox("Mandatory ban on coal burners / tandoor fires" if language == "English" else "कोयले और तंदूर जलाने पर रोक", value=True, disabled=True)
            st.checkbox("Active automated water-sprinklers on unpaved roads" if language == "English" else "सड़कों पर पानी का छिड़काव शुरू", value=True, disabled=True)
        else:
            st.success("🟢 STANDARD NORMAL: NO SPECIAL BANS TRIGGERED" if language == "English" else "🟢 स्थिति सामान्य है: कोई प्रतिबंध नहीं")
            st.write("Environmental indexes are verified safe. Regular regional guidelines applicable." if language == "English" else "वायु गुणवत्ता सूचकांक सुरक्षित हैं।")
            
    with g_col2:
        # MISSING FEATURE 3 RESTORED: CITIZEN REPORT FORM
        st.markdown(f"#### 📸 {'Community Active Incident Reporting' if language=='English' else 'नागरिक घटना रिपोर्टिंग पोर्टल'}")
        st.write("Give normal citizens an app tool to pinpoint illegal burns & trash smoke in real-time." if language == "English" else "नागरिकों को कचरा और अवैध धुआं रिपोर्ट करने की सुविधा।")
        
        with st.form("c_citizen_form"):
            if language == "English":
                st.selectbox("Incident Burn Alert", ["Trash/Waste Burning", "Farm Fire (Stubble)", "Excessive Industrial exhaust", "Severe Construction Dust"])
                st.text_area("Specific Incident Location Details:")
