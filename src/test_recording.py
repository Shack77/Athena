from recording_manager import (
    RecordingManager
)

call_sid = input(
    "Enter Call SID: "
)

manager = RecordingManager()

file_path = (
    manager.download_call_recording(
        call_sid
    )
)

print(
    "Recording saved to:",
    file_path
)