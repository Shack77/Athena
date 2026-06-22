from pathlib import Path


class TranscriptLogger:

    def __init__(self):
        Path("transcripts").mkdir(exist_ok=True)

    def save(self, call_id, transcript):

        filename = Path("transcripts") / f"{call_id}.txt"

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(transcript)

        return filename