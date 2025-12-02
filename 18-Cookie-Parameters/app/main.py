# FastAPI aur Cookie import karo
from fastapi import FastAPI, Cookie
from typing import Annotated

# FastAPI app banao
app = FastAPI()

## Cookie Parameters - cookies se data read karna
@app.get("/products/recommendations")
async def get_recommendations(session_id: Annotated[str | None, Cookie()] = None):
  # Agar session_id hai toh recommendations dikhao
  if session_id:
    return {"message": f"Recommendations for session {session_id}", "session_id": session_id}
  # Nahi toh default recommendations
  return {"message": "No session ID provided, showing default recommendations"}

# Curl command - cookie ke saath request bhejna
# curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/products/recommendations