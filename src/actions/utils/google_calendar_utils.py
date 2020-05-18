# pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client httplib2
# python3 add_event.py --noauth_local_webserver

# Reference: https://developers.google.com/calendar/quickstart/python
# Documentation: https://developers.google.com/calendar/overview

# Be sure to enable the Google Calendar API on your Google account by following the reference link above and
# download the credentials.json file and place it in the same directory as this file.

from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

# print(os.path.abspath(os.path.join(os.path.dirname(__file__),"credentials.json")))

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar"
store = file.Storage("token.json")
creds = store.get()
if (not creds or creds.invalid):
    flow = client.flow_from_clientsecrets(os.path.abspath(os.path.join(
        os.path.dirname(__file__), "credentials.json")), SCOPES)
    creds = tools.run_flow(flow, store)
service = build("calendar", "v3", http=creds.authorize(Http()))


class Google_Calendar_Utils:
    """Google_Calendar_Utils is a utility to use google calendar api in order to add and delete events."""

    def delete(self, record_id):
        """The delete can be used to delete the event on the google calendar based on the record id.


        :param: record_id(int): the record id you want to delete

        """
        # Call the Calendar API.
        now = datetime.utcnow().isoformat() + "Z"  # "Z" indicates UTC time.
        print("Getting the upcoming 10 events.")
        events_result = service.events().list(calendarId="primary", timeMin=now,
                                              maxResults=10, singleEvents=True, orderBy="startTime").execute()
        events = events_result.get("items", [])
        if not events:
            print("No upcoming events found.")
        for event in events:
            # print(event);
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

            temp = event["summary"].split(" ")
            event_record_id = temp[len(temp) - 1]
            if event_record_id == record_id:
                result = service.events().delete(calendarId='primary', eventId=event['id']).execute()
                print(result)
                break

    def insert(self, title, car_location, description, est_rent_date, est_return_date, email):
        """insert can be used to insert the event on the google calendar.

        :param: title(string): the title of the event
        :param: car_location(string): the car location
        :param: description(string): the description to the new evnent
        :param: est_rent_date(string): the rent date
        :param: est_return_date(string): the estimated return date
        :param: email(string): the client's email

        """
        time_start = "{}T{}+10:00".format(est_rent_date.split(" ")[0], est_rent_date.split(" ")[1])
        time_end = "{}T{}+10:00".format(est_return_date.split(" ")[0], est_return_date.split(" ")[1])
        event = {
            "summary": title,
            "location": car_location,
            "description": description,
            "start": {
                "dateTime": time_start,
                "timeZone": "Australia/Melbourne",
            },
            "end": {
                "dateTime": time_end,
                "timeZone": "Australia/Melbourne",
            },
            "attendees": [
                {"email": email},
            ],
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "email", "minutes": 5},
                    {"method": "popup", "minutes": 10},
                ],
            }
        }

        event = service.events().insert(calendarId="primary", body=event).execute()
        print("Event created: {}".format(event.get("htmlLink")))
