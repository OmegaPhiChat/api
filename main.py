from fastapi import FastAPI
import pusher
from dotenv import load_dotenv, find_dotenv
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

load_dotenv(find_dotenv())
AppID = os.getenv("app_id")
Key = os.getenv("key")
Secret = os.getenv("secret")
Cluster = os.getenv("cluster")
pusher_client = pusher.Pusher(app_id = AppID, key = Key, secret = Secret, cluster = Cluster)

@app.post("/join")
async def create_user(username):
    pusher_client.trigger("global", "message", {
        "message": f"{username} has joined"
    })
    return username
