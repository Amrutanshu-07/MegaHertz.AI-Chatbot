# MegaHertz.AI-Chatbot
MegaHertz.AI is a conversational chatbot built with FastAPI (and Streamlit , powered by the Google Gemini API.It provides a modern chat interface where users can interact with an AI assistant.
eatures

1) FastAPI Backend → Handles API calls to Gemini

2) Streamlit Frontend → Interactive chatbot UI

3) Persistent Chat History → Stores conversations locally in JSON

4) Sidebar Controls → Clear chat, view stats, app info

5) Dynamic UI → Chat messages update instantly

# Project Structure
Chatbot/
│── server/                 
│   │── app/
│   │   │── __init__.py
│   │   │── main.py         
│   │   │── ai.py           
│   │   │── schemas.py      
│   │── .env                
│   │── myvenv/             
│
│── frontend/               
│   │── app.py              
│   │── requirements.txt    
│
│── .gitignore
│── README.md

# Setup Instructions
1. Clone the Repository
   git clone https://github.com/<your-username>/Chatbot.git
   cd Chatbot
2. Backend Setup (FastAPI)
   cd server
   python3 -m venv myvenv
   source myvenv/bin/activate   # Linux/macOS
   myvenv\Scripts\activate    # Windows

   pip install fastapi uvicorn aiohttp python-dotenv

3. Add API Key

   Create a .env file inside server/:
   API_KEY=your_gemini_api_key_here
   GEMINI_URL=https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent

  Run Backend
  uvicorn app.main:app --reload
  
4. Frontend Setup
   cd ../frontend
   pip install -r requirements.txt
   streamlit run app.py


# Example Workflow

 1.Start the FastAPI backend
 2.Launch the Streamlit frontend
 3.Ask questions → AI responds via Gemini API
 4.Conversations are saved in chat_history.json

# Requirements

Python 3.9+
Packages:
fastapi
uvicorn
aiohttp
python-dotenv
streamlit
requests

# Notes

1. .env file (with API key) is ignored in Git for security.
2. chat_history.json is ignored to prevent pushing user data.


