# modules/email_utils.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(to_email: str, subject: str, body: str):
    """
    Sends an email using the configured SMTP credentials.
    """
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")

    if not all([smtp_server, smtp_email, smtp_password]):
        print("[Email] Missing SMTP credentials.")
        return False

    try:
        msg = MIMEMultipart()
        msg["From"] = smtp_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))  # allows HTML body

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
        
        print(f"[Email] Sent to {to_email}: {subject}")
        return True
    except Exception as e:
        print(f"[Email][Error] {e}")
        return False
