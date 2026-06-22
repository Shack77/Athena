from scenarios import SCENARIOS
from call_runner import CallRunner


def main():

    scenario = SCENARIOS[0]

    runner = CallRunner(
        scenario
    )

    print()
    print("Scenario:")
    print(scenario["title"])
    print()

    while True:

        athena = input(
            "ATHENA: "
        )

        if athena.lower() in [
            "quit",
            "exit",
            "done"
        ]:
            break

        runner.add_athena_message(
            athena
        )

        patient_reply = (
            runner.generate_patient_reply()
        )

        print()
        print(
            "PATIENT:",
            patient_reply
        )
        print()

    call_id, report = (
        runner.finish()
    )

    print()
    print("Call ID:", call_id)
    print("Score:",
          report.get(
              "overall_score"
          ))
    print()


if __name__ == "__main__":
    main()