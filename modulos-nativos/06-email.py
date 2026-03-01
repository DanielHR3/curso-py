from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from smtplib import SMTP

path = Path("modulos-nativos/shooter.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje['From'] = "danielhrubio3@gmail.com"
mensaje['To'] = "danielhrubio3@gmail.com"
mensaje['Subject'] = "Probando el módulo email"
cuerpo = MIMEText("Hola, este es un mensaje de prueba utilizando el módulo email de Python.", 'plain')
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("danielhrubio3@gmail.com", "vqwjdeijmjrghjea")
    smtp.send_message(mensaje)
    print("Correo enviado exitosamente.")
