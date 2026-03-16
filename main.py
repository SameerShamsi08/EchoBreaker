from fastapi import FastAPI, UploadFile
from transcriber import transcribe_audio
from idea_extractor import extract_ideas

app = FastAPI()

@app.post("/analyze_meeting")

async def analyze_meeting(file: UploadFile):

    path = f"temp/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    transcript = transcribe_audio(path)

    ideas = extract_ideas(transcript)

    return {
        "transcript": transcript,
        "ideas": ideas
    }
