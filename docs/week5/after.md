# Static analysis after the refactor

| Measure | Before (`legacy_fees.py`) | After (`fees.py`) |
| --- | --- | --- |
| Ruff issues (total) | 17 | 0 |
| Highest cyclomatic complexity | 9 (`calc`) | 4 (`tuition_fee` and `report`) |
| Arguments of the main function | 6 | 5 |
| Pylint score (/10) | 4.86 | 10.00 |
| Tests passing | 0 (no tests) | 21 (10 grade and 11 fee tests) |

Ruff 0.17.6 reported `PLR0917` for the original positional parameter count, bringing the baseline to 17 diagnostics. The fee tests compare the refactored calculation against the original starter and check that a scholarship student receives the correct fee in either student order.

The expanded suite adds the handout’s four comparison cases and its 18-credit reduction check. For the scholarship category, the characterization case retains the legacy summer surcharge of 150. The regular-term batch regression expects Omar to pay 0 in both student orders.

## Pairing reflection

The grade boundaries give the driver and navigator a clear checklist for review. The scholarship case shows why a navigator should try the same input in a different order. Running the characterization tests after each small change gives the next driver a quick way to check the handoff.

Each participant's account of the 12-minute rotations and any issue they caught is pending.
