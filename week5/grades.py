"""Convert numeric scores to letter grades."""


def letter_grade(score: int) -> str:
    """Return the letter grade for a score from 0 to 100."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100 inclusive")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
