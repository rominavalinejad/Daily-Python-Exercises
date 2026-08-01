# 01-Error-Handling
## Challenge: Server Port Config Validator

1. Implement a utility function that accepts a server network port value as an input (handling both string and integer types).
2. Catch any ValueError exceptions smoothly to prevent application crashes when non-numeric strings are provided, returning a professional error message.
3. Set strict business logic rules to validate that the numeric port falls within the standard networking range of 1 to 65535.
4. Encapsulate all execution workflows and comprehensive test parameters inside a dedicated main() entry-point function.
5. Maintain clean execution scopes to completely avoid polluting the global namespace with temporary tracking variables.

### Code Quality & Linting
This module strictly complies with PEP 8 style guidelines and architectural standards:
* Pylint Score: 10.00/10
* Key Fixes: Implemented full docstrings, cleaned trailing spaces, and restricted variable visibility to the local function environment.

# 02-Error-Handling
## Challenge: CSV Data Pipeline with Bad-Row Quarantine

1. Implement a utility function validate_row() to check input user dictionaries against strict rules (non-empty name, integer age between 0 and 100, and valid email structural syntax).
2. Catch any ValueError exceptions smoothly during record parsing to prevent application crashes when bad or corrupted CSV lines are encountered.
3. Build a robust quarantine routing system that writes verified clean records to valid_users.csv and isolates invalid rows with line tracking into quarantine.log.
4. Encapsulate multi-file I/O context operations and dictionary reading/writing workflows cleanly inside a dedicated process_data() function.
5. Maintain standard execution scopes with a modular main() entry-point to completely avoid polluting the global namespace with temporary runtime variables.

### Code Quality & Linting
This module strictly complies with PEP 8 style guidelines and architectural standards:
* Pylint Score: 10.00/10
* Key Fixes: Added concise function docstrings, streamlined multi-file context manager indentations, and separated validation logic from data pipeline operations.

