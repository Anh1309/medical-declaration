from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
import os

def send_email(email):
    img_data = open('qr.png', 'rb').read()
    from_email = "testttttt.139@gmail.com"
    from_password = "664666222"
    to_email = email

    msg = MIMEMultipart()
    subject = "Medical Declaration"
    message = MIMEText("Scan this QR code to see your medical declaration")
    msg.attach(message)

    image = MIMEImage(img_data, name=os.path.basename('qr.png'))
    msg.attach(image)
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.ehlo()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)