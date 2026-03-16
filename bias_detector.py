def detect_bias(transcript):

    prompt = f"""
    Analyze this discussion and detect cognitive biases.

    Transcript:
    {transcript}

    Detect:
    - Confirmation Bias
    - Survivorship Bias
    - Overconfidence Bias
    - Groupthink
    """

    response = model.generate_content(prompt)

    return response.text
