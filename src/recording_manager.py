import os
import time
import requests
from pathlib import Path

from twilio.rest import Client

from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN
)


class RecordingManager:

    def __init__(self):

        self.client = Client(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN
        )

        Path("recordings").mkdir(
            exist_ok=True
        )

    def wait_for_recording(self, call_sid, timeout=60):

        recordings = self.client.recordings.list(limit=20)

        print("Found recordings:", len(recordings))

        for r in recordings:
            print(
            "SID:", r.sid,
            "CALL:", r.call_sid
        )

        return recordings[0]

    def download_recording(
        self,
        recording_sid,
        filename=None
    ):

        if filename is None:

            filename = (
                f"recordings/{recording_sid}.mp3"
            )

        recording = (
            self.client.recordings(
                recording_sid
            ).fetch()
        )

        recording_url = (
            f"https://api.twilio.com"
            f"{recording.uri.replace('.json', '.mp3')}"
        )

        response = requests.get(
            recording_url,
            auth=(
                TWILIO_ACCOUNT_SID,
                TWILIO_AUTH_TOKEN
            )
        )

        response.raise_for_status()

        with open(
            filename,
            "wb"
        ) as f:

            f.write(response.content)

        return filename

    def download_call_recording(
        self,
        call_sid
    ):

        recording = (
            self.wait_for_recording(
                call_sid
            )
        )

        return self.download_recording(
            recording.sid
        )