from patient_agent import PatientAgent
from call_session import CallSession


class ConversationManager:

    def __init__(self, scenario):

        self.scenario = scenario

        self.patient = PatientAgent(
            scenario
        )

        self.session = CallSession(
            scenario
        )

    def process_athena_message(
        self,
        athena_text
    ):

        self.session.add_message(
            "ATHENA",
            athena_text
        )

        history = []

        for msg in self.session.messages:

            role = (
                "user"
                if msg["speaker"] == "ATHENA"
                else "assistant"
            )

            history.append(
                {
                    "role": role,
                    "content": msg["text"]
                }
            )

        reply = self.patient.generate_reply(
            history
        )

        self.session.add_message(
            "PATIENT",
            reply
        )

        return reply