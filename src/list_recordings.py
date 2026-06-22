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
    limit=20
)

print("Recordings Found:", len(recordings))

for r in recordings:

    print(
        "Recording SID:", r.sid
    )

    print(
        "Call SID:", r.call_sid
    )

    print("-" * 50)