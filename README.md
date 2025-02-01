## Servicio de Correo Electrónico SMTP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este proyecto es un servicio de correo electrónico basado en Python que utiliza FastAPI Mail y plantillas Jinja2 para enviar correos electrónicos. 

El servicio se utiliza para manejar la seccion de contactos de mi portfolio personal. Link al portfolio: [https://francoleondev.vercel.app/](https://francoleondev.vercel.app/)

Por cada solicitud POST al endpoint `/send-email`, el servicio envía un correo electrónico al destinatario especificado en el cuerpo de la solicitud y al correo especificado en las variables de entorno como `MAIL_DEVELOPER`.

### Requisitos Previos

- Python 3.7+
- pip
- Un servidor SMTP válido

### Instalación

1. Clona el repositorio:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala los paquetes requeridos:
    ```sh
    pip install -r requirements.txt
    ```

4. Crea un archivo `.env` en el directorio raíz y agrega la configuración de tu servidor SMTP:
    ```env
    MAIL_USERNAME=tu_email@example.com
    MAIL_PASSWORD=tu_contraseña
    MAIL_PORT=587
    MAIL_SERVER=smtp.example.com
    MAIL_FROM=tu_email@example.com
    MAIL_DEVELOPER=developer_email@example.com
    ```

### Endpoints

- **GET /**

    Devuelve un mensaje indicando que el servicio de correo electrónico está en funcionamiento.

    **Respuesta:**
    ```json
    {
        "message": "Email service is running"
    }
    ```

- **POST /send-email**

    Envía un correo electrónico utilizando los datos proporcionados en la solicitud.

    **Cuerpo de la solicitud:**
    ```json
    {
        "name": "Nombre del Usuario",
        "email": "user@example.com",
        "description": "Esta es una descripción."
    }
    ```

    **Respuesta:**
    ```json
    {
        "message": "Email sent successfully"
    }
    ```

    **Errores:**
    - **500 Internal Server Error:** Ocurre un error al enviar el correo electrónico.
    ```json
    {
        "detail": "An error occurred while sending the email: <error_message>"
    }
    ```

### Licencia

Este proyecto está licenciado bajo la Licencia MIT.