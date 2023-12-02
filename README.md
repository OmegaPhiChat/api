# api

This is the api server for OmegaPhiChat.

The tech stack used is FastAPI, Python, and Pusher.

App is deployed at https://omega-phi-chat.fly.dev/

## Getting Started

1. Run `uvicorn main:app --reload`
2. Create `.env` file and include the Pusher credentials.

```
PUSHER_APP_ID =
PUSHER_KEY =
PUSHER_SECRET =
PUSHER_CLUSTER =
WEB_URL =
```
