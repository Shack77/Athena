from speech_to_text import SpeechToText

stt = SpeechToText()

text = stt.transcribe(
    "sample.wav"
)

print(text)