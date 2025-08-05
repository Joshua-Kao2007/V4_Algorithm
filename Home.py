# Page: Welcome
import streamlit as st

# Page config
st.set_page_config(page_title="HGO Internal Acquisitions Algorithm", layout="wide")

# Title
st.title("HGO BI Acquisitions Algorithm")

# Subtitle and brief intro
st.markdown("### Meet Aria: AI-powered Donor Prospecting Solicitation! 👋")
st.markdown("""
We’re currently in **Version 4** of the Aria (Audience Relationship Intelligence Algorithm).

Our system has been extensively trained on historical giving, historical engagement, public affinity, wealth data, and demographical data from constituents among others. 
""")

# Feature bullets
st.markdown("""
Aria:
- 📊 **Leverages historical data** — including engagement patterns, public wealth signals, and donor trajectories to train accurate prediction models  
- 🧠 **Classifies new constituents in real-time**, telling us they're likelihood to become donors and the lifecycle stage they belong to (Dormant, Interested, Engaged, or Active Donor)  
- 💡 **Recommends solicitation strategies** personalized to each individual — including optimal outreach channel, timing, and messaging style  
- 🔁 **Continuously learns and improves**, updating predictions based on new interactions and real results  
- 🛠️ Built with **Streamlit**, **scikit-learn**, and **Tessitura-integrated pipelines** by **Joshua Kao**. Documentation and User Manual still in progress. 
""")

# Button to move to Aria page
if st.button("🚀 Get started: View Donor Insights!"):
    st.switch_page("pages/1_View_Donor_Insights!.py")
if st.button("Train Model (Admin Only) "):
    st.switch_page("pages/2_Train_Model.py")


# Footer
st.markdown("---")
st.markdown("**Created by Joshua Kao**, © 2025", unsafe_allow_html=True)
