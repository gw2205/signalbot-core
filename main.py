# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SignalBot Core", version="0.1.0")

# Optional CORS middleware (allowing all for dev purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SignalBot is live 🟢"}

# You can later add routes here from:
# - sentibot sentiment scanner
# - signalbot evaluator
# - guard filters
# - telegram push
# - historical signal logs
