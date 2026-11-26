import pytest

from fees import Course, StudentType, process_all, tuition_fee
from legacy_fees import calc


def test_regular_student_pays_for_all_course_hours():
    courses = [Course(3), Course(2)]
    legacy_fee = calc([{"h": 3}, {"h": 2}], 1, 2026, False, None)
    assert tuition_fee(courses, StudentType.REGULAR) == legacy_fee == 1750


def test_staff_child_pays_half():
    courses = [Course(3)]
    legacy_fee = calc([{"h": 3}], 2, 2026, False, None)
    assert tuition_fee(courses, StudentType.STAFF_CHILD) == legacy_fee == 525


def test_scholarship_has_no_base_tuition():
    courses = [Course(3)]
    legacy_fee = calc([{"h": 3}], 3, 2026, False, None)
    assert tuition_fee(courses, StudentType.SCHOLARSHIP) == legacy_fee == 0


def test_summer_and_high_tuition_adjustments_match_legacy():
    courses = [Course(20)]
    legacy_courses = [{"h": 20}]
    assert (
        tuition_fee(courses, StudentType.REGULAR)
        == calc(legacy_courses, 1, 2026, False, None)
        == 6800
    )
    assert (
        tuition_fee(courses, StudentType.REGULAR, summer=True)
        == calc(legacy_courses, 1, 2026, True, None)
        == 6950
    )


def test_discount_and_extras_match_legacy():
    courses = [Course(3)]
    extras = (25, 40)
    assert (
        tuition_fee(courses, StudentType.REGULAR, discount=100, extras=extras)
        == calc([{"h": 3}], 1, 2026, False, 100, extras)
        == 1015
    )


def test_scholarship_student_is_not_skipped():
    students = [
        {"name": "Sara", "type": 1, "courses": [Course(3)], "summer": False},
        {"name": "Omar", "type": 3, "courses": [Course(3)], "summer": False},
    ]
    expected = {"Sara": 1050, "Omar": 0}
    assert process_all(students) == expected
    assert process_all(list(reversed(students))) == expected


@pytest.mark.parametrize(
    ("hours", "code", "kind", "summer"),
    [
        ((3, 3, 3), 1, StudentType.REGULAR, False),
        ((3, 3, 3, 3, 3, 3), 1, StudentType.REGULAR, True),
        ((3, 4), 2, StudentType.STAFF_CHILD, False),
        ((3, 3), 3, StudentType.SCHOLARSHIP, True),
    ],
)
def test_handout_cases_match_legacy(hours, code, kind, summer):
    legacy_courses = [{"h": hour} for hour in hours]
    courses = [Course(hour) for hour in hours]

    assert tuition_fee(courses, kind, summer) == calc(
        legacy_courses, code, 2026, summer, None
    )


def test_eighteen_hours_gets_large_fee_reduction():
    assert tuition_fee([Course(6), Course(6), Course(6)], StudentType.REGULAR) == 6100
