# Original invoice smells

| Smell | Where | Principle | Refactoring |
| --- | --- | --- | --- |
| Fee-type conditionals | Branches inside and after the course loop | OCP. Each new fee type requires editing the calculation. | Register separate policies in a lookup. |
| Mixed responsibilities | `make_invoice` calculates, formats, writes and prints | SRP. Pricing, formatting and output have different reasons to change. | Put fee rules in policies, file output in a writer and display in the caller. |
| Hard-coded storage | `open(...)` inside `make_invoice` | DIP. The calculation depends directly on the filesystem. | Accept an object with a `write(student_id, text)` method. |
| Manual resource management | `open`, `write`, then `close` | Resource safety. An exception during writing can skip `close`. | Use a context manager in `FileWriter`. |
| Magic numbers | Tuition rates, scholarship multiplier and service fee | Readability. Raw numbers hide business rules. | Name the constants. |
| Repeated per-course pricing | Loop over `student.courses` | Simplicity. Each fee policy depends on total credit hours. | Pass `student.total_hours` to the selected policy once. |

Characterization tests check both returned fees and stored invoice text for a six-credit student. The totals are 7,200 EGP for regular students, 3,600 EGP for scholarships, and 17,000 EGP for international students. The refactor follows the handout's policy lookup and leaves printing to the caller. The sibling test expects 5,400 EGP and verifies the injected writer output. The sibling commit changes the discount constant, policy and lookup entry. It leaves `make_invoice` untouched.
