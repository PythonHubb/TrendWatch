from trendwatch.validation import validate_topic, validate_score
import pytest


def test_validate_topic():
    result = validate_topic("  AI  ")
    assert result == "AI"


def test_validate_score():
    result = validate_score(85)
    assert result == 85.0


def test_validate_score_out_of_range():
    with pytest.raises(ValueError):
        validate_score(150)


def test_validate_topic_empty():
    with pytest.raises(ValueError):
        validate_topic("   ")


def test_validate_score_negative():
    with pytest.raises(ValueError):
        validate_score(-10)


def test_validate_score_zero():
    result = validate_score(0)
    assert result == 0.0


def test_validate_score_maximum():
    result = validate_score(100)
    assert result == 100.0


def test_validate_score_invalid_type():
    with pytest.raises(ValueError):
        validate_score("hello")