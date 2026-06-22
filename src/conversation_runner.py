from patient_agent import PatientAgent
from scenarios import SCENARIOS

scenario = SCENARIOS[0]

agent = PatientAgent(scenario)

history = []

while True:

    athena = input("ATHENA: ")

    history.append(
        {
            "role": "user",
            "content": athena
        }
    )

    reply = agent.generate_reply(history)

    print("\nPATIENT:", reply)

    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )