from os import environ as env

# 3rd party imports
from twilio.rest import Client

# Twilio Config
ACCOUNT_SID = env.get('ACCOUNT_SID')
AUTH_TOKEN = env.get('AUTH_TOKEN')
SERVICE_ID = env.get('SERVICE_ID')

# Create a Twilio client using account_sid and auth token
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send(message_body, contact_list):
    response = client.notify.services(SERVICE_ID).notifications.create(
        to_binding=contact_list,
        body=message_body)

    return response if response.sid else None
