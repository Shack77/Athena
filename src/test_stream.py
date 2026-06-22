print("Starting test...")

from twilio_caller import TwilioCaller

print("Imported caller")

caller = TwilioCaller()

print("Created caller")

call_sid = caller.start_stream_call()

print("CALL SID:", call_sid)