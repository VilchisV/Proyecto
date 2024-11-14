# correo.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Correo:
    @staticmethod
    def enviar_email(destinatario, asunto, mensaje):
        remitente = "tu_email@ejemplo.com"
        password = "tu_contraseña"
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(remitente, password)
            server.send_message(msg)
