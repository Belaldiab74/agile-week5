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
