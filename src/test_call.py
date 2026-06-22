from twilio_caller import TwilioCaller

caller = TwilioCaller()

call_sid = caller.make_test_call()

print("Call SID:", call_sid)