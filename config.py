import os

from dotenv import load_dotenv

load_dotenv()

base_email_address = os.getenv("base_email_address")
email_app_password = os.getenv("email_app_password")
