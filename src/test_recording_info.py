from twilio.rest import Client
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN
)

client = Client(
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN
)

recordings = client.recordings.list(
    limit=1
)

r = recordings[0]

print("SID:", r.sid)
print("URI:", r.uri)