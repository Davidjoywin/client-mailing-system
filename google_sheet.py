import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


api_key = "AIzaSyDSZPmZ759vhn6yctYKYSdOq1R2w2mk4mU"

a = {
    "web":
    {
        "client_id":"706642481479-7uur6l8l998mffe6kk4c3qk6rhgsf3nv.apps.googleusercontent.com",
        "project_id":"coinbyte-380721",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":"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"
    }
}

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1qO3cwIWGkABtUQSimzFU2WwO5WDcGQSsU3FFHaxiJbA"

def googleSheet():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            print(flow)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A1:F2").execute()
        values = result.get("values", [])

        return values
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    googleSheet()