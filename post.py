import requests
import smtplib
from email.message import EmailMessage
import os

SENDER_EMAIL = os.environ["SENDER_ACCOUNT"]
SENDER_PASSWORD = os.environ["SENDER_PASSWORD"]
RECEIVER = os.environ["RECEIVING_EMAIL"]

class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(url=self.blog_url)
        self.msg = EmailMessage()

    def get_all_blog_post(self):
        self.response.raise_for_status()
        return self.response.json()

    def get_specific_post(self, blog_num):
        self.response.raise_for_status()
        blog = self.response.json()
        num = int(blog_num) - 1
        return blog[num]

    def send_message(self, user_name, user_email, user_number, user_message):
        self.msg['Subject'] = f"Hello from {user_name}"
        self.msg['From'] = SENDER_EMAIL
        self.msg['To'] = RECEIVER
        self.msg.set_content(f'Name: {user_name}\nNumber: {user_number}\nEmail: {user_email}\nMessage: {user_message}')

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.send_message(self.msg)

        print("Message Sent Successfully!")


