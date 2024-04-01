"""
Read contacts from csv and send email.
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv

def send_email():
    # set up the SMTP server
    smtp_server = smtplib.SMTP(host='your-smtp-server.com', port=587)
    smtp_server.starttls()
    smtp_server.login("your-email@example.com", "your-password")

    # read the recipient emails from a CSV file
    with open('recipients.csv', 'r') as f:
        reader = csv.reader(f)
        recipients = list(reader)

    for recipient in recipients:
        # create a message
        msg = MIMEMultipart()
        msg['From'] = "your-email@example.com"
        msg['To'] = recipient[0]
        msg['Subject'] = "This is a test email"

        # add the email body
        message = "Hello, this is a test email sent from a Python script."
        msg.attach(MIMEText(message, 'plain'))

        # add an attachment
        filename = "path-to-your-file"
        attachment = open(filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

        # send the message
        smtp_server.send_message(msg)

    smtp_server.quit()

# Example usage:
if __name__ == "__main__":
    send_email()
