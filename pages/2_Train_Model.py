import streamlit as st
import pandas as pd
from ml_engine.model_training import run_adaboost_on_all

st.set_page_config(page_title="Admin Model Training", layout="wide")
st.title("🔐 Admin: Train AdaBoost Models")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Enter admin password:", type="password")
    if st.button("Enter"):
        if password == "password":
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password.")

if st.session_state.authenticated:
    st.success("✅ Access granted.")

    if st.button("🚀 Train All AdaBoost Models"):
        try:
            results = run_adaboost_on_all()

            for r in results:
                st.markdown(f"### 📄 Results for `{r['filename']}`")
                st.write("Confusion Matrix:")
                st.write(r["confusion_matrix"])
                st.write("Classification Report:")
                st.json(r["report"])

                df_probs = pd.DataFrame({
                    "True Label": r["y_true"].values,
                    "Predicted": r["y_pred"],
                    "Probability (Patron+)": r["y_proba"]
                })
                st.write("🔍 Prediction Probabilities:")
                st.dataframe(df_probs)

        except Exception as e:
            st.error(f"❌ Error during training: {e}")
