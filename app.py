import streamlit as st
import openai

# Set page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot (Powered by OpenAI)")
st.write("This is a fully functional AI chatbot demo.")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# API Key input (keep private)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# User input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Send request to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    bot_response = response["choices"][0]["message"]["content"]

    # Save conversation
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_response))

# Display conversation
for sender, msg in st.session_state.history:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")

