# 🌬️ SWAAS: Proactive Air-Quality Network & Action (OS)

**Hackathon Theme:** Help people breathe easier. Track what's in the air, warn the people most exposed to it, and change what happens on the bad days.

## ⚠️ The Problem
Current Air Quality Index (AQI) apps are passive—they only tell you the air is bad when it's already too late. During stubble burning seasons or industrial smog spikes, vulnerable citizens (like children and asthma patients) are exposed to hazardous air without immediate, actionable interventions. 

## 💡 Our Solution: PRANA OS
SWAAS is not just an AQI dashboard; it is a **complete ecosystem** that Tracks, Warns, and Acts. We focus on the Malwa Region (Indore, Dhar, Ujjain, etc.) to provide micro-climate tracking and automate interventions before the toxic plumes arrive.

### 🚀 Key Features

*   🌍 **Live Regional Threat Map:** Tracks active farm fires and visualizes the predictive path of smoke plumes across districts.
*   🏫 **IoT School Automation:** Simulates an ESP32 micro-controller network that automatically turns on classroom air purifiers, shuts ventilation, and cancels outdoor P.E. classes when outdoor AQI breaches safe limits.
*   🫁 **Health Impact & SMS Gateway:** Translates invisible PM2.5 data into understandable metrics (e.g., "Breathing today's air equals smoking 4 cigarettes") and dispatches targeted SMS alerts only to registered vulnerable patients.
*   🌾 **Farmer Carbon Wallet (Stubble-to-Wealth):** A positive reinforcement tool that calculates how much a farmer can earn (via Carbon Credits and Biomass sales) if they sell their stubble instead of burning it.
*   🏛️ **Automated GRAP (Govt. Action Center):** Automatically triggers legal restrictions (like banning construction or heavy trucks) the moment city AQI crosses critical thresholds.

## 🛠️ Tech Stack
*   **Frontend & UI:** Streamlit (Python)
*   **Data Processing:** Pandas, NumPy
*   **Mapping:** Streamlit Native Mapping
*   **Simulated Hardware:** IoT Relay logic for ESP32

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/akshatjain129/SWAAS-air-os.git](https://github.com/akshatjain129/SWAAS-air-os.git)
