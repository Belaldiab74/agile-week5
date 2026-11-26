# Legacy fee findings

Ruff reported 17 diagnostics and Pylint scored the original starter 4.86/10. The starter matches the code printed in the Week 5 handout.

| Rule | Count | Smell (lecture name) | Refactoring |
|---|---:|---|---|
| F401 | 2 | Dead code (unused imports) | Delete the imports |
| PLR2004 | 6 | Magic numbers | Replace with named constants or an enum |
| C901 | 1 | Long Method / complex conditional | Use a fee-share table and a separate reporting function |
| PLR0913 | 1 | Long Parameter List | Drop the unused year argument and give optional inputs defaults |
| PLR0917 | 1 | Long Parameter List | Drop the unused year argument |
| ARG001 | 1 | Dead code (unused argument) | Remove `y` from the signature and call sites |
| B006 | 1 | Mutable default argument | Use an empty tuple for extras |
| E711 / E712 | 1 / 1 | Clumsy comparisons | Default the discount to zero and test summer directly |
| F841 | 1 | Dead code (unused variable) | Delete the `tmp` assignment |
| N802 | 1 | Bad naming | Rename `ProcessAll` to `process_all` |

## Smells found by inspection

- Names such as `d`, `c`, and `st` conceal the meanings of course and student data.
- The regular and staff child branches in `ProcessAll` repeat the same calculation call.
- `report` and `ProcessAll` mix fee calculation with printing, which makes the results harder to reuse.

## Scholarship bug

Omar is a scholarship student and should pay 0 for the given courses, but neither type branch in `ProcessAll` assigns his fee. With Sara first, the output is `Sara 1050` followed by `Omar 1050` because the loop reuses Sara's fee. With Omar first, the print statement raises `UnboundLocalError` for `fee`, matching Pylint diagnostic `E0606`.
