"""Convert numeric scores to letter grades."""

MIN_SCORE = 0
MAX_SCORE = 100
GRADE_THRESHOLDS = ((90, "A"), (80, "B"), (70, "C"), (60, "D"))


def letter_grade(score: int) -> str:
    """Return the letter grade for a score from 0 to 100."""
    if not MIN_SCORE <= score <= MAX_SCORE:
        raise ValueError(f"Score must be between {MIN_SCORE} and {MAX_SCORE} inclusive")

    for threshold, grade in GRADE_THRESHOLDS:
        if score >= threshold:
            return grade
    return "F"
