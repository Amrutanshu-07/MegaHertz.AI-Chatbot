import streamlit as st
import requests
import os
import json
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8000/chat"
CHAT_HISTORY_FILE = "chat_history.json"  

st.set_page_config(
    page_title="MegaHertz.AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_chat_history(messages):
    with open(CHAT_HISTORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)

if "messages" not in st.session_state:
    st.session_state["messages"] = load_chat_history()


with st.sidebar:
    st.title("MegaHertz.AI 🤖")
    st.markdown("**Settings & Options**")
    

    if st.button("🧹 Clear Chat"):
        st.session_state["messages"] = []
        save_chat_history(st.session_state["messages"])
        st.experimental_rerun()
    
    st.markdown("---")
    st.markdown("**About**")
    st.info("MegaHertz.AI is a chatbot powered by Gemini API and FastAPI backend. 💡")
    

    st.markdown("---")
    st.markdown(f"**Total messages:** {len(st.session_state['messages'])}")

st.title("⚡ MegaHertz.AI - Chatbot")
st.markdown("Ask me anything powered by **Gemini API** 🚀")

# Chat container
chat_container = st.container()

with chat_container:
    for msg in st.session_state["messages"]:
        role = "🧑 You" if msg["role"] == "user" else "🤖 MegaHertz.AI"
        with st.chat_message(msg["role"]):
            st.markdown(f"**{role}:** {msg['content']}")

def send_message(prompt):
    
    st.session_state["messages"].append({"role": "user", "content": prompt, "timestamp": str(datetime.now())})
    
  
    with st.chat_message("user"):
        st.markdown(f"**🧑 You:** {prompt}")

 
    try:
        response = requests.post(BACKEND_URL, json={"message": prompt})
        if response.status_code == 200:
            bot_reply = response.json().get("response", "⚠️ No response")
        else:
            bot_reply = f" Error {response.status_code}: {response.text}"
    except Exception as e:
        bot_reply = f" Backend connection error: {str(e)}"
    

    st.session_state["messages"].append({"role": "assistant", "content": bot_reply, "timestamp": str(datetime.now())})
    
    with st.chat_message("assistant"):
        st.markdown(f"**🤖 MegaHertz.AI:** {bot_reply}")
    

    save_chat_history(st.session_state["messages"])

if prompt := st.chat_input("Type your message..."):
    send_message(prompt)
