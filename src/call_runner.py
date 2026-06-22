from datetime import datetime

from patient_agent import PatientAgent
from evaluator import Evaluator
from report_writer import ReportWriter
from transcript_logger import TranscriptLogger


class CallRunner:

    def __init__(self, scenario):

        self.scenario = scenario

        self.patient = PatientAgent(
            scenario
        )

        self.evaluator = Evaluator()

        self.report_writer = ReportWriter()

        self.transcript_logger = (
            TranscriptLogger()
        )

        self.conversation = []

    def build_history(self):

        history = []

        for msg in self.conversation:

            if msg["speaker"] == "ATHENA":

                history.append(
                    {
                        "role": "user",
                        "content": msg["text"]
                    }
                )

            else:

                history.append(
                    {
                        "role": "assistant",
                        "content": msg["text"]
                    }
                )

        return history

    def add_athena_message(self, text):

        self.conversation.append(
            {
                "speaker": "ATHENA",
                "text": text
            }
        )

    def generate_patient_reply(self):

        history = self.build_history()

        reply = self.patient.generate_reply(
            history
        )

        self.conversation.append(
            {
                "speaker": "PATIENT",
                "text": reply
            }
        )

        return reply

    def build_transcript(self):

        lines = []

        for msg in self.conversation:

            lines.append(
                f"{msg['speaker']}:\n{msg['text']}\n"
            )

        return "\n".join(lines)

    def finish(self):

        call_id = datetime.now().strftime(
            "call_%Y%m%d_%H%M%S"
        )

        transcript = (
            self.build_transcript()
        )

        self.transcript_logger.save(
            call_id,
            transcript
        )

        report = self.evaluator.evaluate(
            transcript
        )

        self.report_writer.save_all(
            call_id,
            report
        )

        return call_id, report