from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

@app.get("/news")
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    return response.json()
