# Copilot Instructions for AI Agents

This codebase is a single-file Python project (`lab nomer 1.py`) containing solutions to several small tasks, each focused on basic input/output and conditional logic. The project is intended for educational or lab work purposes, with all logic in one script.

## Project Structure
- All code is in `lab nomer 1.py`.
- No external dependencies or build steps are required.
- No test files or automation scripts are present.

## Key Patterns & Conventions
- Each task is separated by comments (e.g., `#task 112`, `#task 137`, `#task 162`).
- User input is handled via `input()`; output is printed directly.
- Ukrainian language is used for prompts and some variable names.
- Tasks are independent; variables and logic do not overlap between tasks.
- Error handling is minimal, but present for input parsing (see `try/except` for banknote denomination).

## Example Task Structure
```python
#task 162
banknotes = { ... }
try:
    denomination = int(input(...))
    person = banknotes.get(denomination)
    if person:
        print(...)
    else:
        print(...)
except ValueError:
    print(...)
```

## Developer Workflow
- Run the script directly with Python (no arguments needed):
  ```powershell
  python "lab nomer 1.py"
  ```
- No build, test, or lint commands are required.
- Debug by commenting/uncommenting task sections as needed.

## Recommendations for AI Agents
- When adding new tasks, follow the comment-based separation and input/output style.
- Use Ukrainian for user-facing messages to match existing conventions.
- Keep all logic in the single script unless instructed otherwise.
- If refactoring, preserve the independence of each task section.

## No External Integrations
- The project does not use external libraries, APIs, or frameworks.
- No cross-file communication or modularization is present.

---
If any conventions or workflows are unclear, ask the user for clarification before making changes.
