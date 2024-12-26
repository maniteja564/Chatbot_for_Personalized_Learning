import streamlit as st
import requests

# Rasa API endpoint (change the port if needed)
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# Set up the Streamlit app
st.title("Chat with Rasa Bot")

# Input box for the user to type their message
user_message = st.text_input("You:", "")

# Container to display conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to send user message to Rasa API
def send_message_to_rasa(message):
    payload = {"message": message}
    response = requests.post(RASA_URL, json=payload)
    return response.json()

# Function to handle and display conversation
def display_conversation():
    if user_message:
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to Rasa
        bot_response = send_message_to_rasa(user_message)

        # Add bot response to session state
        for response in bot_response:
            st.session_state.messages.append({"role": "bot", "content": response.get("text", "No response.")})

    # Display the conversation
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"**You:** {message['content']}")
        else:
            st.write(f"**Bot:** {message['content']}")

# Display conversation
display_conversation()

# Button to clear conversation history
if st.button("Clear Conversation"):
    st.session_state.messages = []
