import streamlit as st
from predict import predict

st.title("📧 Email Spam Classifier")
st.write("Paste an email below to check whether it is spam or ham.")

text = st.text_area("Email content", height=200)

if st.button("Check"):
    if text.strip() == "":
        st.warning("Please enter some email text first.")
    else:
        result = predict(text)
        if result == "Spam":
            st.error("🚨 This email is SPAM")
        else:
            st.success("✅ This email is HAM (legitimate)")
