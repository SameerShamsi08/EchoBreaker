def generate_report(ideas, counter_args, bias):

    report = f"""
    ECHOBREAKER DEVIL'S ADVOCATE REPORT

    Ideas Proposed
    ---------------
    {ideas}

    Counter Arguments
    -----------------
    {counter_args}

    Cognitive Biases Detected
    -------------------------
    {bias}

    Recommendation
    ---------------
    Reconsider strategy before execution.
    """

    return report
