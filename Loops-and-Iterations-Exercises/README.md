# 01-Loops-and-Iterations
## Challenge: Secure Authentication & Login System

1. Define a secure system password and initialize a maximum limit of 3 login attempts.
2. Create a dynamic loop that continuously prompts the user to enter their password as long as they have remaining attempts.
3. Implement conditional logic to validate the user's input against the correct system password.
4. If the password is correct, display a clear success message ("Access Granted") and instantly terminate the loop using a break statement.
5. If the password is incorrect, decrement the available attempts by 1 and provide real-time console feedback showing the remaining attempts.
6. Once all attempts are exhausted without a successful login, lock the system and display a terminal alert ("Access Denied / Account Locked").

# 02-Loops-and-Iterations
## Challenge: Dynamic Smart Waste Categorization System

1. Implement an infinite management loop (while True) that acts as an enterprise-level operator console.
2. Prompt the operator to enter the total number of items to process per batch, with an option to type 'finish' to safely shut down the system.
3. Include strict input validation (.isdigit()) to prevent system crashes from accidental non-numeric inputs.
4. Dynamically iterate from 1 to the user-specified limit using a nested for loop.
5. Apply specific multi-condition business logic (if-elif-else) to auto-classify waste based on ID divisibility:
   - Divisible by both 3 and 5 -> "E-Waste" [High Priority]
   - Divisible by 3 -> "Plastic Materials" [Recyclable]
   - Divisible by 5 -> "Paper & Cardboard" [Recyclable]
   - Any other ID -> "Organic Waste" [Standard]
6. Display a fully aligned, real-time visual report using string formatting techniques (:02d) for optimal enterprise output design.

# 03-Loops-and-Iterations
## Challenge: Email Filter and Cleaner

1. Define a list containing various unformatted, valid, invalid, and spam email strings.
2. Initialize three empty lists (`valid_emails`, invalid_emails, and `spam_emails`) to categorize the processed results.
3. Iterate over the raw_emails list using a loop, cleaning each email by stripping whitespace and converting text to lowercase.
4. Implement conditional logic (`if-elif-else`) to classify emails based on spam keywords (`marketing`, spam`) and validation checks (presence of `@` and `.`).
5. Append each processed email to its corresponding list and print the categorized results clearly line by line.
