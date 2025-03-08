import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔒🔑Password Strength Checker!")

st.markdown("""
## Welcome to the Ultimate Password Strength Checker! 
Ensure your password is secure by checking:
- ✅ Length
- ✅ Upper & Lowercase letters
- ✅ Numbers
- ✅ Special Characters

⚡ *Improve your online security by creating strong passwords!*  
""")

password = st.text_input("Enter your password", type = "password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both **upper and lower case characters.**")
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least **one digit.**")
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least **one special character(!@#$%&*).**")
    if score == 4:
        feedback.append("✅Your password is **strong.**")
    elif score == 3:
        feedback.append("🟡 Your password is **moderately strong.**")
    else:
        feedback.append("🔴 Your password is **weak.** Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions.")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your **password.**")


