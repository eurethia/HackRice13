# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = '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'
audio_file= open("tst2.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)