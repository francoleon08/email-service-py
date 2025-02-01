import os
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import FileSystemLoader, Environment

load_dotenv()

template_loader = FileSystemLoader(searchpath="./templates")
template_env = Environment(loader=template_loader)


async def handler_send_email(email: str, name: str, description: str):
    template_response = template_env.get_template('response.html')
    template_details = template_env.get_template('details.html')

    html_content_response = template_response.render(name=name)
    html_content_details = template_details.render(name=name, email=email, description=description)

    message_response = MessageSchema(
        subject="Franco Leon - Desarrollador de Software",
        recipients=[email],
        body=html_content_response,
        subtype='html',
    )

    message_details = MessageSchema(
        subject="Detalles de la solicitud de contacto de " + name,
        recipients=[os.getenv('MAIL_DEVELOPER')],
        body=html_content_details,
        subtype='html',
    )

    connection_config = ConnectionConfig(
        MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
        MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
        MAIL_PORT=int(os.getenv('MAIL_PORT')),
        MAIL_SERVER=os.getenv('MAIL_SERVER'),
        MAIL_FROM=os.getenv('MAIL_FROM'),
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False
    )

    fm = FastMail(connection_config)
    await fm.send_message(message_response)
    await fm.send_message(message_details)
