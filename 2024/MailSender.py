import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def send_email(recipient_email, subject, body):
    # Get credentials from environment variables
    sender_email = os.environ.get("EMAIL_USER")
    app_password = os.environ.get("EMAIL_PASSWORD")

    # Check if credentials are available
    if not sender_email or not app_password:
        raise ValueError("Email credentials not found in environment variables")

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    try:
        # Create SMTP session
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            # Login to account
            server.login(sender_email, app_password)

            # Send email
            server.send_message(message)

        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    recipient = "itanbarasan@gmail.com"
    subject = "Test Email"
    content = "This is a test email sent from Python!"

    send_email(recipient, subject, content)
