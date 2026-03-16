from faster_whisper import WhisperModel

model = WhisperModel("base")

def transcribe_audio(file_path):

    segments, info = model.transcribe(file_path)

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript
