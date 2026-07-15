# app.py

import streamlit as st
import time
from datetime import datetime
from chatbot import get_response

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🤖 Rule-Based AI Chatbot")

st.caption(
    "A simple chatbot that uses predefined responses to answer common questions, provide information, and perform basic interactions."
)

st.markdown("---")

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("💡 Available Commands")

    commands = [
        "hi",
        "hello",
        "hey",
        "how are you",
        "who are you",
        "what is your name",
        "what can you do",
        "developer",
        "who created you",
        "date",
        "time",
        "what is ai",
        "what is machine learning",
        "what is python",
        "joke",
        "quote",
        "help",
        "bye"
    ]

    for command in commands:
        st.write(f"• {command}")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! How can I assist you today?",
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]
        st.session_state.pending_response = False
        st.rerun()

# -----------------------------
# Initialize Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! How can I assist you today?",
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]

if "pending_response" not in st.session_state:
    st.session_state.pending_response = False

# -----------------------------
# Display Messages
# -----------------------------
for message in st.session_state.messages:

    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(
                f"<b>You:</b> {message['content']} "
                f"<sub style='color:gray'>{message['time']}</sub>",
                unsafe_allow_html=True
            )

    else:
        with st.chat_message("assistant"):
            st.markdown(
                f"<b>Bot:</b> {message['content']} "
                f"<sub style='color:gray'>{message['time']}</sub>",
                unsafe_allow_html=True
            )

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
            "time": datetime.now().strftime("%I:%M %p")
        }
    )

    st.session_state.pending_response = True
    st.rerun()

# -----------------------------
# Generate Bot Response
# -----------------------------
if st.session_state.pending_response:

    last_message = st.session_state.messages[-1]

    if last_message["role"] == "user":

        with st.spinner("Bot is typing..."):
            time.sleep(1.5)

        response = get_response(last_message["content"])

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
                "time": datetime.now().strftime("%I:%M %p")
            }
        )

        st.session_state.pending_response = False
        st.rerun()