import streamlit as st
import random

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

st.title("🌱 Growth Mindset Challenge")
st.write("Click the button below to get your next growth challenge!")

challenges = [
    "📘 Learn something new for 20 minutes today.",
    "🧠 Replace 'I can't' with 'I will try'.",
    "📝 Write down one thing you’re grateful for.",
    "🎯 Set one small goal and complete it today.",
    "🚶‍♂️ Take a 10-minute walk and reflect on your progress.",
    "💬 Give someone a genuine compliment.",
    "📚 Read 5 pages of a book that inspires you.",
    "❓ Ask a 'why' question about something you don’t understand.",
    "🧘‍♀️ Meditate for 5 minutes with full focus.",
    "🔄 Reframe one negative thought into a positive one."
]

if st.button("✨ New Challenge"):
    st.success(random.choice(challenges))
else:
    st.info("Press the button to begin your growth journey!")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
