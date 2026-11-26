"""Tuition calculation and reporting for SET 312 Lab 5."""

from dataclasses import dataclass
from enum import IntEnum


class StudentType(IntEnum):
    """Student categories used to determine tuition shares."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass(frozen=True)
class Course:
    """A course with its number of billable hours."""

    hours: int


RATE_PER_HOUR = 350
HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150

FEE_SHARE = {
    StudentType.REGULAR: 1,
    StudentType.STAFF_CHILD: 0.5,
    StudentType.SCHOLARSHIP: 0,
}


def tuition_fee(courses, kind, summer=False, discount=0, extras=()):
    """Calculate tuition with the legacy adjustments applied in order."""
    total_hours = sum(course.hours for course in courses)
    total = total_hours * RATE_PER_HOUR * FEE_SHARE[kind]
    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE
    total -= 0 if discount is None else discount
    for charge in extras:
        total += charge
    return total


def report(courses, kind, summer=False, discount=0):
    """Return the fee report text for one student."""
    fee = tuition_fee(courses, kind, summer, discount)
    lines = []
    if kind == StudentType.REGULAR:
        lines.append(f"Student fee: {fee}")
    elif kind == StudentType.STAFF_CHILD:
        lines.append(f"Staff child fee: {fee}")
    if fee > HIGH_FEE_THRESHOLD:
        lines.append("High fee")
    return "\n".join(lines)


def process_all(students):
    """Return a fee for every student, keyed by name."""
    return {
        student["name"]: tuition_fee(
            student["courses"], StudentType(student["type"]), student["summer"]
        )
        for student in students
    }


def print_fees(fees):
    """Print each student name and its calculated fee."""
    for name, fee in fees.items():
        print(name, fee)
