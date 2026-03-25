from fastapi import FastAPI
from pydantic import BaseModel
from search import search_tavily
from query import generate_query

app = FastAPI()

class ClaimRequest(BaseModel):
    claim: str

@app.get("/")
def home():
    return {"message": "Multi-Agent Fact Checking System Running"}

@app.post("/check")
def check_claim(request: ClaimRequest):
    query = generate_query(request.claim)
    results = search_tavily(query)

    return {
        "claim": request.claim,
        "generated_query": query,
        "results": results
    }