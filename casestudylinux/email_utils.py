import smtplib  #Handles sending emails using SMTP
import bcrypt   #Provides securely stored passwords
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  #helips to format email mesgs

def get_email_credentials():
    """Get email credentials from the user without hiding the password."""
    sender_email = input("Enter sender email: ")
    receiver_email = input("Enter receiver email: ")
    plain_password = input("Enter email password: ")  # Password visible for debugging

    # Hash the password with salt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt)

    print("Credentials Captured")
    print(f"Sender Email: {sender_email}")
    print(f"Receiver Email: {receiver_email}")
    print(f"Hashed Password: {hashed_password}")

    return sender_email, receiver_email, plain_password, hashed_password

def send_email(sender_email, receiver_email, plain_password, subject, body):
    """Send an email notification."""
    msg = MIMEMultipart()  #creates am email msg
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))


    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        print("Connecting to SMTP Server...")

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrades the connection to a secure encrypted one.
        print("Secure Connection Established")

        print("Logging in with the provided credentials")
        server.login(sender_email, plain_password)

        print("Sending Email...")
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email and password.")
    except Exception as e:
        print(f"Error: {e}")
