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


class FileWriter:
    """Write the invoice text to the default local file."""

    def write(self, student_id, text):
        with open(f"invoice_{student_id}.txt", "w", encoding="utf-8") as file:
            file.write(text)


def make_invoice(student, kind, writer=None):
    """Return the fee and save the invoice through the selected writer."""
    total = POLICIES[kind].fee(student.total_hours)
    text = f"Invoice for {student.student_id}: {int(total)} EGP"
    invoice_writer = FileWriter() if writer is None else writer
    invoice_writer.write(student.student_id, text)
    return total
