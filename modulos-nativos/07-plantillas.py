import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from smtplib import SMTP
from string import Template

# ========= CONFIG =========
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

FROM_EMAIL = "danielhrubio3@gmail.com"
TO_EMAIL = "chimenea_9792@hotmail.com"
SUBJECT = "Para ti, Ximena 💛"

TEMPLATE_PATH = Path("modulos-nativos/plantilla.html")
FOTO_PATH = Path("modulos-nativos/mimenita.png")


if not TEMPLATE_PATH.exists():
    raise FileNotFoundError(f"No existe plantilla: {TEMPLATE_PATH.resolve()}")

if not FOTO_PATH.exists():
    raise FileNotFoundError(f"No existe imagen: {FOTO_PATH.resolve()}")

# ========= HTML desde archivo =========
plantilla = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
html = plantilla.substitute(
    titulo="Para ti, Ximena 💛",
    firma="Daniel",
)

# ========= ARMAR MENSAJE =========
mensaje = MIMEMultipart("related")
mensaje["From"] = FROM_EMAIL
mensaje["To"] = TO_EMAIL
mensaje["Subject"] = SUBJECT

mensaje.attach(MIMEText(html, "html", "utf-8"))

mime_image = MIMEImage(FOTO_PATH.read_bytes())
mime_image.add_header("Content-ID", "<foto_xime>")
mime_image.add_header("Content-Disposition", "inline", filename=FOTO_PATH.name)
mensaje.attach(mime_image)

# ========= ENVIAR =========
with SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("danielhrubio3@gmail.com", "vqwjdeijmjrghjea")
    smtp.send_message(mensaje)
    print("Correo enviado exitosamente.")
