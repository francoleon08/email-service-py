from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from EmailService import handler_send_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):
    name: str
    email: EmailStr
    description: str


@app.get("/")
async def root(request: Request):
    client_domain = request.headers.get("X-Client-Domain")  # Leer el dominio enviado
    print(f"Dominio del cliente: {client_domain}")
    return {"message": "Email service is running"}


@app.post("/send-email")
async def send_email(request: EmailRequest):
    try:
        await handler_send_email(request.email, request.name, request.description)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while sending the email: {str(e)}")
