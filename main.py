from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from EmailService import handler_send_email

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):
    name: str = Field(..., title="Full Name", min_length=1)
    email: EmailStr = Field(..., title="Email Address")
    description: str = Field(..., title="Description", min_length=1)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send-email")
async def send_email(request: EmailRequest):
    try:
        await handler_send_email(request.name, request.email, request.description)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while sending the email: {str(e)}")
