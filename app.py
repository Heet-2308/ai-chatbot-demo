import streamlit as st
import openai

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot (Powered by OpenAI)")

if "history" not in st.session_state:
    st.session_state.history = []

# Use secrets for API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Use the current ChatCompletion method
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
        )
        bot_response = response.choices[0].message.content
    except Exception as e:
        bot_response = f"Error: {e}"

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_response))

for sender, msg in st.session_state.history:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")


   

