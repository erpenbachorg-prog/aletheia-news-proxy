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
    url = url = f"https://newsapi.org/v2/top-headlines?q=politik&language=de&apiKey=9e78d47e0a434b178bcfdbe2c30daca8"
    return requests.get(url).json()
