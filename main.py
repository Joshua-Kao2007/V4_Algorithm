import streamlit as st

# Page config
st.set_page_config(page_title="HGO Internal Acquisitions Algorithm", layout="wide")

# Title
st.title("HGO Internal Acquisitions Algorithm")

# Subtitle and brief intro
st.markdown("### Hi there, welcome 👋")
st.markdown("""
We’re currently in **Version 4** of the HGO Internal Acquisitions Algorithm.

Our system has been extensively trained on historical giving, affinity, and engagement data from constituents.
""")

# Feature bullets
st.markdown("""
- 📊 **Extensive training data** covering engagement history, wealth signals, and donor trajectories  
- 🧠 **Predictive modeling** to classify whether a newly entered constituent is likely to become a donor  
- 💡 **Solicitation suggestions** tailored to the classified profile (e.g. timing, message type, channel)  
- 🛠️ Built with **Streamlit**, **scikit-learn**, and **Tessitura-integrated pipelines**  
""")

# Footer
st.markdown("---")
st.markdown("**Created by Joshua Kao**, © 2025", unsafe_allow_html=True)
