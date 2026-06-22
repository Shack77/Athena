from scenarios import SCENARIOS
from patient_agent import PatientAgent
from evaluator import Evaluator
from report_writer import ReportWriter
from transcript_logger import TranscriptLogger


class BatchRunner:

    def __init__(self):

        self.evaluator = Evaluator()

        self.report_writer = ReportWriter()

        self.transcript_logger = TranscriptLogger()

    def run_scenario(self, scenario):

        print(
            f"\nRunning: {scenario['id']}"
        )

        patient = PatientAgent(
            scenario
        )

        conversation = []

        # Simulated Athena opening
        athena_message = (
            "Thank you for calling. "
            "How may I help you today?"
        )

        conversation.append(
            {
                "speaker": "ATHENA",
                "text": athena_message
            }
        )

        for _ in range(10):

            history = []

            for msg in conversation:

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

            patient_reply = (
                patient.generate_reply(
                    history
                )
            )

            conversation.append(
                {
                    "speaker": "PATIENT",
                    "text": patient_reply
                }
            )

            # Temporary Athena simulation
            athena_reply = (
                "Can you provide more details?"
            )

            conversation.append(
                {
                    "speaker": "ATHENA",
                    "text": athena_reply
                }
            )

        transcript = self.build_transcript(
            conversation
        )

        self.transcript_logger.save(
            scenario["id"],
            transcript
        )

        report = (
            self.evaluator.evaluate(
                transcript
            )
        )

        self.report_writer.save_all(
            scenario["id"],
            report
        )

        return report

    def build_transcript(
        self,
        conversation
    ):

        lines = []

        for msg in conversation:

            lines.append(
                f"{msg['speaker']}:\n"
                f"{msg['text']}\n"
            )

        return "\n".join(lines)

    def run_all(self):

        for scenario in SCENARIOS:

            try:

                report = (
                    self.run_scenario(
                        scenario
                    )
                )

                print(
                    f"Score: "
                    f"{report.get('overall_score')}"
                )

            except Exception as e:

                print(
                    f"Failed: "
                    f"{scenario['id']}"
                )

                print(e)


if __name__ == "__main__":

    runner = BatchRunner()

    runner.run_all()