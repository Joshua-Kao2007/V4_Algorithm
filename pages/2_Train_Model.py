import streamlit as st

st.set_page_config(page_title="Admin Login", layout="centered")
st.title("🔐 Admin Login")

# Admin password input
password = st.text_input("Enter admin password to access model training:", type="password")

# Standard button (not automatic)
if st.button("Enter"):
    if password == "your_secret_password":  # 🔒 Replace with secure password or use st.secrets
        st.success("✅ Access granted! Redirecting...")
        st.switch_page("_AdminTrainModel.py")
    elif password:
        st.error("❌ Incorrect password.")
