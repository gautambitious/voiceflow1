from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import Flask,jsonify,request,render_template
from flask_restful import Resource, Api, reqparse


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def reminder(date,slot):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    event = {
      'summary': 'appointment with doctor',
      'location': '',
      'description': 'visit doctor and get yourself checked',
      'start': {
        'dateTime': '2020-05-11T09:00:30-00:30',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2020-05-11T09:00:30-00:30',
        'timeZone': 'America/Los_Angeles',
      },
      'recurrence': [
        ''
      ],
      'attendees': [
        {'email': 'pradyumn25jain@gmail.com'}

      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    try:
    	event = service.events().insert(calendarId='primary', body=event).execute()
    	print('Event created: %s' % (event.get('htmlLink')))
    	return "event created"
    except:
    	return "something went wrong"







def main():


    date = "23"
    slot = "3"

    if "3" in slot:
      slot == 0
    if "4" in slot:
      slot == 1
    else:
      slot == 2

    print("status {}".format(reminder(int(date),int(slot))))

 
    

if __name__ == '__main__':
    main()

