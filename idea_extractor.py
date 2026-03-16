import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro")

def extract_ideas(transcript):

    prompt = f"""
    Extract the main strategic ideas from this meeting transcript.

    Transcript:
    {transcript}

    Return bullet points.
    """

    response = model.generate_content(prompt)

    return response.text



