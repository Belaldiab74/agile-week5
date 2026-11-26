# SET 312 TDD, BDD and refactoring

The uploaded Lab 7 PDF uses **Lab 6** internally, so the source is under [lab6](../../lab6) and the submission material is here.

1. [Git log for the four TDD cycles](tdd-git-log.txt). The GitHub Actions history check runs each cycle's tests with the preceding implementation and then with that cycle's implementation.
2. [Task A1 coverage answer](coverage-answer.md).
3. [Registration feature](../../lab6/features/registration.feature), including the drop scenario.
4. [Task C1 smells table](invoice-smells.md) and [Task C2 invoice refactor](../../lab6/invoice.py).
5. [Part D campus maintenance scenarios](campus-maintenance.feature). “Report a campus maintenance issue” is a proposed backlog story for the team's campus maintenance project.

To run Parts A–C from the repository root:

```sh
cd lab6
python -m pip install pytest pytest-cov behave ruff
python -m pytest --cov=registration --cov-report=term-missing --cov-fail-under=100
python -m behave
python -m ruff check .
```

The Part D feature specifies acceptance criteria for the planned application.
