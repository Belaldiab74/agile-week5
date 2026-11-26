"""Calculate and save fee invoices for enrolled students."""

FEE_PER_HOUR = 1200
SCHOLARSHIP_FRACTION = 0.5
INTERNATIONAL_RATE = 2000
INTERNATIONAL_SERVICE_FEE = 5000


class RegularPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR


class ScholarshipPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR * SCHOLARSHIP_FRACTION


class InternationalPolicy:
    def fee(self, hours):
        return hours * INTERNATIONAL_RATE + INTERNATIONAL_SERVICE_FEE


POLICIES = {
    "regular": RegularPolicy(),
    "scholarship": ScholarshipPolicy(),
    "international": InternationalPolicy(),
}


def make_invoice(student, kind):
    total = POLICIES[kind].fee(student.total_hours)
    text = f"Invoice for {student.student_id}: {int(total)} EGP"
    with open(f"invoice_{student.student_id}.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print(text)
    return total
