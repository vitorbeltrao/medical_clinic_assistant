import streamlit as st

from src.utils import chat_iteration
from src.prompts import SYSTEM_PROMPT

st.title("Chatbot Clínica Médica")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

prompt = st.chat_input(
    "Digite sua mensagem..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        response = chat_iteration(
            messages=st.session_state.messages
        )

        st.write(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
