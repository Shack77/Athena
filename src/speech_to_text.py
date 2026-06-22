from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)


class SpeechToText:

    def transcribe(
        self,
        audio_file_path
    ):

        with open(
            audio_file_path,
            "rb"
        ) as audio_file:

            transcript = (
                client.audio.transcriptions.create(
                    model="gpt-4o-mini-transcribe",
                    file=audio_file
                )
            )

        return transcript.text