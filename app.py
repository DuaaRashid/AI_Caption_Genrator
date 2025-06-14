import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
# ---- Load Gemini Model ----
model = genai.GenerativeModel("gemini-2.0-flash")


#streamlitUI
st.set_page_config(page_title="AI Caption Genrator",page_icon="📸")
st.title("AI Caption Generator")
st.write("✨ Enter a topic or mood and get 5 creative, catchy captions!")
topic=st.text_input("📝 Topic (e.g. sunset, coffee vibes, fitness motivation):")

if st.button("Generate captions"):
    if not topic.strip():
     st.warning("Please enter a topic first!")
    else:
        with st.spinner("Thinking of awesome captions..."):
            prompt=f"Write 5 short, creative, catchy Instagram captions (with emojis) for this topic: {topic}"
            response= model.generate_content(prompt)

            st.success("Here are your captions: ")
            captions = response.text.strip().split('\n')
            for cap in captions:
                if cap.strip():
                 st.markdown(f"- {cap.strip()}")
        st.caption("💡 Tip: Refresh the button for more creative results!")