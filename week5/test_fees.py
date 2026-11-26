import pytest

from fees import Course, tuition_fee
from legacy_fees import calc


@pytest.mark.parametrize(
    ("hours", "code", "summer", "expected"),
    [
        ((3, 3, 3), 1, False, 3150),
        ((3, 3, 3, 3, 3, 3), 1, True, 6250),
        ((3, 4), 2, False, 1225),
        ((3, 3), 3, True, 150),
    ],
)
def test_characterize_legacy_tuition(hours, code, summer, expected):
    courses = [{"h": hour} for hour in hours]
    assert calc(courses, code, 2026, summer, None) == expected
    assert tuition_fee([Course(hour) for hour in hours], code, summer) == expected
