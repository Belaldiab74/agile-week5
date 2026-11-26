from dataclasses import dataclass
from enum import IntEnum


class StudentType(IntEnum):
    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass(frozen=True)
class Course:
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
    hours = sum(course.hours for course in courses)
    total = hours * RATE_PER_HOUR * FEE_SHARE[kind]
    if total > HIGH_FEE_THRESHOLD:
        total = total - HIGH_FEE_REDUCTION
    if summer:
        total = total + SUMMER_SURCHARGE
    total = total - (0 if discount is None else discount)
    for charge in extras:
        total = total + charge
    return total


def report(courses, kind, summer=False, discount=0):
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
    fees = {}
    for student in students:
        if student["type"] == StudentType.REGULAR:
            fee = tuition_fee(
                student["courses"], StudentType.REGULAR, student["summer"]
            )
        if student["type"] == StudentType.STAFF_CHILD:
            fee = tuition_fee(
                student["courses"], StudentType.STAFF_CHILD, student["summer"]
            )
        fees[student["name"]] = fee
    return fees


def print_fees(fees):
    for name, fee in fees.items():
        print(name, fee)
