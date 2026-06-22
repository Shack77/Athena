from patient_agent import PatientAgent
from scenarios import SCENARIOS
from evaluator import Evaluator
from report_writer import ReportWriter


def conversation_to_transcript(conversation):

    transcript = []

    for msg in conversation:

        transcript.append(
            f"{msg['speaker']}:\n{msg['text']}\n"
        )

    return "\n".join(transcript)


def main():

    scenario = SCENARIOS[0]

    patient = PatientAgent(scenario)

    evaluator = Evaluator()

    writer = ReportWriter()

    conversation = []

    print("\n===================================")
    print("Scenario:", scenario["title"])
    print("Goal:", scenario["goal"])
    print("===================================\n")

    while True:

        athena_message = input("ATHENA: ")

        if athena_message.lower() in [
            "exit",
            "quit",
            "done"
        ]:
            break

        conversation.append(
            {
                "speaker": "ATHENA",
                "text": athena_message
            }
        )

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

        patient_reply = patient.generate_reply(
            history
        )

        print("\nPATIENT:", patient_reply)
        print()

        conversation.append(
            {
                "speaker": "PATIENT",
                "text": patient_reply
            }
        )

    transcript = conversation_to_transcript(
        conversation
    )

    print("\n========== TRANSCRIPT ==========\n")
    print(transcript)

    report = evaluator.evaluate(
        transcript
    )

    files = writer.save_all(
        "call_001",
        report
    )

    print("\n========== REPORT ==========\n")
    print(report)

    print("\nSaved Files:")
    print(files)


if __name__ == "__main__":
    main()