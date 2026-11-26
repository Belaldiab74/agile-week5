import pytest

from invoice import make_invoice
from registration import Student


@pytest.fixture
def student():
    student = Student("2023001")
    student.register("SET312", 3)
    student.register("SET472", 3)
    return student


@pytest.mark.parametrize(
    ("kind", "expected"),
    [
        ("regular", 7200),
        ("scholarship", 3600),
        ("international", 17000),
    ],
)
def test_invoice_total_and_saved_text(student, kind, expected, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    assert make_invoice(student, kind) == expected
    assert (tmp_path / "invoice_2023001.txt").read_text(encoding="utf-8") == (
        f"Invoice for 2023001: {expected} EGP"
    )


class FakeWriter:
    def __init__(self):
        self.saved = {}

    def write(self, student_id, text):
        self.saved[student_id] = text


def test_invoice_uses_injected_writer(student):
    writer = FakeWriter()

    assert make_invoice(student, "regular", writer=writer) == 7200

    assert writer.saved == {"2023001": "Invoice for 2023001: 7200 EGP"}


def test_sibling_fee_is_25_percent_off_regular_fee(student):
    writer = FakeWriter()

    assert make_invoice(student, "sibling", writer=writer) == 5400

    assert writer.saved == {"2023001": "Invoice for 2023001: 5400 EGP"}
