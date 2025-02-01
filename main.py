from fastapi import FastAPI
from EmailService import send_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://francoleondev.vercel.app"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send-email")
async def say_hello(name: str, email: str, description: str):
    await send_email(name, email, description)
    return {"message": "Email sent successfully"}
