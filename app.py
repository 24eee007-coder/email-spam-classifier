import streamlit as st
from predict import predict

st.title("📧 Email Spam Classifier")
st.write("Email text-a keezha paste pannu, spam-a ham-a nu check pannalaam.")

text = st.text_area("Email content", height=200)

if st.button("Check"):
    if text.strip() == "":
        st.warning("Munnadi email text type pannu.")
    else:
        result = predict(text)
        if result == "Spam":
            st.error("🚨 Idhu SPAM")
        else:
            st.success("✅ Idhu HAM (normal email)")