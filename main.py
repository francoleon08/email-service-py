from fastapi import FastAPI
from EmailService import handler_send_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send-email")
async def send_email(name: str, email: str, description: str):
    await handler_send_email(name, email, description)
    return {"message": "Email sent successfully"}
