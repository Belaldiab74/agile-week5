"""Course registration for the Student Services App."""


class RegistrationError(Exception):
    """A registration or drop request violated a rule."""


class Student:
    """A student and the courses on their timetable."""

    def __init__(self, student_id):
        self.student_id = student_id
        self.courses = {}

    @property
    def total_hours(self):
        """Return the number of registered credit hours."""
        return sum(self.courses.values())

    def register(self, code, hours):
        """Register a course with its credit hours."""
        self.courses[code] = hours
