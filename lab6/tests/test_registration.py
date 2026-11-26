import pytest

from registration import RegistrationError, Student


def test_register_adds_hours():
    student = Student("2023001")

    student.register("SET312", 3)

    assert student.total_hours == 3


def test_cannot_go_over_18_hours():
    student = Student("2023001")
    student.register("SET312", 15)

    with pytest.raises(RegistrationError, match="credit-hour limit is 18"):
        student.register("SET472", 4)

    assert student.total_hours == 15
    assert "SET472" not in student.courses


def test_cannot_register_same_course_twice():
    student = Student("2023001")
    student.register("SET312", 3)

    with pytest.raises(RegistrationError, match="already registered"):
        student.register("SET312", 4)

    assert student.total_hours == 3


def test_drop_removes_course():
    student = Student("2023001")
    student.register("SET312", 3)

    student.drop("SET312")

    assert student.total_hours == 0


def test_cannot_drop_a_course_that_is_not_registered():
    student = Student("2023001")
    student.register("SET312", 3)

    with pytest.raises(RegistrationError, match="SET472 is not registered"):
        student.drop("SET472")

    assert student.courses == {"SET312": 3}
