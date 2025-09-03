import streamlit as st

st.set_page_config(page_title="AI Chatbot Demo", page_icon="🤖")

st.title("🤖 AI Chatbot Demo")
st.write("This is a simple chatbot demo for my portfolio.")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    if "hello" in user_input.lower():
        bot_response = "Hi there! 👋 How can I help you today?"
    elif "price" in user_input.lower():
        bot_response = "This is just a demo — but I can connect to real data."
    else:
        bot_response = "I'm still learning. 🙂"
    
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_response))

# Display conversation
for sender, msg in st.session_state.history:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
