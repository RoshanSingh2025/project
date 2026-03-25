from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Multi-Agent Fact Checking System Running"}

@app.post("/check")
def check_claim(claim: str):
    return {
        "claim": claim,
        "status": "Processing pipeline will be added in Day 2"
    }