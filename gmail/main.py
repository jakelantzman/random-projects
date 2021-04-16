from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import tkinter as tk
import sys

import Email
import School
import Weather


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    #Class calls
    email = Email(service)
    inbox = email.batchEmails() #list
    
    school = School()
    assignments = school.getAssignments() #list 

    weather = Weather()
    today = weather.getWeather() #list 

    # -----------------------------
    # TKINTER CODE BELOW THIS POINT 
    # -----------------------------

    window = tk.Tk()
    #window.geometry('1280x1024')
    window.attributes('-fullscreen', True)
    window.configure(bg='black')

    #Close on escape key
    def close(event):
        window.withdraw() # if you want to bring it back
        sys.exit() # if you want to exit the entire thing

    window.bind('<Escape>', close)
    window.mainloop()


