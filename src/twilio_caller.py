from twilio.rest import Client

from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    ATHENA_TEST_NUMBER
)


class TwilioCaller:

    def __init__(self):

        self.client = Client(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN
        )

    def start_stream_call(self):

        websocket_url = (
         "wss://detonator-playtime-capped.ngrok-free.dev/media-stream"
    )   

        twiml = f"""
<Response>
    <Connect>
        <Stream url="{websocket_url}" />
    </Connect>
</Response>
"""

        print(twiml)

        call = self.client.calls.create(
        to=ATHENA_TEST_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        twiml=twiml
    )

        print(f"Call Started: {call.sid}")

        return call.sid

    def get_call_status(
        self,
        call_sid
    ):

        call = (
            self.client.calls(
                call_sid
            ).fetch()
        )

        return call.status

    def hangup_call(
        self,
        call_sid
    ):

        self.client.calls(
            call_sid
        ).update(
            status="completed"
        )

        print(
            f"Call Ended: {call_sid}"
        )