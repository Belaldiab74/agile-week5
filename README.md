# SET 312 Lab 5

Pair-programming kata and static-analysis refactor for Agile Software Engineering.

## Run the lab

From the `week5` directory, create and activate a virtual environment, then run the checks.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install ruff pylint pytest
python -m pytest
python -m ruff check fees.py grades.py test_fees.py test_grades.py
python -m pylint fees.py
```

In Windows PowerShell, skip activation and use `.\.venv\Scripts\python.exe` in place of `python` for the last four commands.

The baseline diagnostics, findings, and final measurements are in [docs/week5](docs/week5/).
