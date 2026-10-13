
def validate_topic(topic: str) -> str:
    if not isinstance(topic, str):
        raise ValueError("Topic must be a string")

    topic = topic.strip()

    if not topic:
        raise ValueError("Topic cannot be empty")

    return topic


def validate_score(score: float) -> float:
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError("Score must be a number")

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")

    return float(score)
