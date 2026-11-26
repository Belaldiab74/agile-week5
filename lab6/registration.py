"""Course registration for the Student Services App."""


MAX_HOURS = 18


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
        if code in self.courses:
            raise RegistrationError(f"{code} is already registered")
        if self.total_hours + hours > MAX_HOURS:
            raise RegistrationError(f"credit-hour limit is {MAX_HOURS}")
        self.courses[code] = hours
