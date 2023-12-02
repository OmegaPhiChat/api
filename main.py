from fastapi import FastAPI, Response
from fastapi.requests import Request
from fastapi.responses import JSONResponse
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

@app.get("/")
async def index():
    return "Hello Buddha"

@app.post("/join")
async def create_user(username):
    pusher_client.trigger("global", "message", {
        "message": f"{username} has joined"
    })
    content = username
    response = JSONResponse(content= content)
    response.set_cookie(key="username", value=username)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.post("/message")
async def create_message(message,request: Request, response: Response):
    name = request.cookies.get("username")
    pusher_client.trigger("global", "message", {
        "message": f"{name}:{message}"
    })
    response.headers["Access-Control-Allow-Origin"] = "*"
