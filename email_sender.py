import smtplib
import csv
from email.message import EmailMessage
from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT

def send_emails():
    with open("contacts.csv", newline="") as file:
        reader = csv.DictReader(file)

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        for row in reader:
            try:
                msg = EmailMessage()
                msg["From"] = EMAIL
                msg["To"] = row["email"]
                msg["Subject"] = f"Hello {row['name']}!"

                msg.set_content(f"Hi {row['name']},\nThis is an automated email.")

                server.send_message(msg)

                with open("email_log.txt", "a") as log:
                    log.write(f"Sent to {row['email']}\n")

            except Exception as e:
                with open("email_log.txt", "a") as log:
                    log.write(f"Failed {row['email']} - {e}\n")

        server.quit()

send_emails()
