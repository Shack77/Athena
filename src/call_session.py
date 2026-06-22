from datetime import datetime


class CallSession:

    def __init__(self, scenario):

        self.scenario = scenario

        self.started_at = datetime.now()

        self.messages = []

        self.completed = False

    def add_message(
        self,
        speaker,
        text
    ):

        self.messages.append(
            {
                "speaker": speaker,
                "text": text,
                "timestamp": datetime.now().isoformat()
            }
        )

    def build_transcript(self):

        lines = []

        for message in self.messages:

            lines.append(
                f"{message['speaker']}: "
                f"{message['text']}"
            )

        return "\n".join(lines)

    def mark_complete(self):

        self.completed = True