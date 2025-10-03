import os
import aiohttp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
GEMINI_URL = os.getenv("GEMINI_URL")

if not API_KEY:
    raise ValueError("❌ API_KEY not found in .env file")

if not GEMINI_URL:
    raise ValueError("❌ GEMINI_URL not found in .env file")


async def get_gemini_response(user_message: str) -> str:
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {"parts": [{"text": user_message}]}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{GEMINI_URL}?key={API_KEY}", json=payload, headers=headers) as resp:
            if resp.status == 200:
                data = await resp.json()
                try:
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                except Exception:
                    return "⚠️ No valid response from Gemini."
            else:
                return f"❌ Error: {resp.status} - {await resp.text()}"
