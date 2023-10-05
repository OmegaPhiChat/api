from fastapi import FastAPI
import pusher
from dotenv import load_dotenv, find_dotenv
import os

app = FastAPI()

load_dotenv(find_dotenv())

pusher_client = pusher.Pusher(
    app_id = os.getenv("PUSHER_APP_ID"),
    key = os.getenv("PUSHER_KEY"),
    secret = os.getenv("PUSHER_SECRET"),
    cluster = os.getenv("PUSHER_CLUSTER")
)

@app.post("/join")
async def create_user(username):
    pusher_client.trigger("global", "message", {
        "message": f"{username} has joined"
    })
    return username
