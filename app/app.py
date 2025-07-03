# app/app.py
import streamlit as st
import pandas as pd
from email_verifier import verify_email_and_domain
from lead_scoring import score_lead_from_url

st.set_page_config(page_title="Caprae Lead Tools", layout="centered")

st.title("🚀 Caprae Lead Tools")
st.markdown("### ✅ Email & Domain Verifier + 🔥 Lead Scorer")

# Email Verifier
st.header("1️⃣ Email & Domain Verifier")
email = st.text_input("Enter Email to Verify:")

format_status, domain_status = "", ""
if email:
    format_status, domain_status = verify_email_and_domain(email)
    st.write(f"Email Format: {format_status}")
    st.write(f"Domain Status: {domain_status}")

# Lead Scorer
st.header("2️⃣ Hot Lead Scoring")
url = st.text_input("Enter Website URL (e.g., https://example.com):")

score, found_keywords = 0, []
if url:
    score_result = score_lead_from_url(url)
    score = score_result[0]
    found_keywords = score_result[1]

    st.success(f"Lead Score: {score}/15")

    if score >= 6:
        st.markdown("🔥 This lead looks HOT!")
    elif score >= 3:
        st.markdown("🟡 Medium-interest lead.")
    else:
        st.markdown("🔵 Cold lead.")

    if found_keywords:
        st.markdown("**Keywords found:** " + ", ".join(found_keywords))

# Optional: Download CSV
if email and url and format_status == "✅ Valid format" and domain_status == "✅ Active":
    lead_data = {
        "Email": [email],
        "Domain": [email.split("@")[-1]],
        "Lead Score": [score],
        "Keywords Found": [", ".join(found_keywords)],
        "Website": [url]
    }
    df = pd.DataFrame(lead_data)
    st.download_button("📥 Download Lead as CSV", df.to_csv(index=False), file_name="lead.csv", mime="text/csv")
