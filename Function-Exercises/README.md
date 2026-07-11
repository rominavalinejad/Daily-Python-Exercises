# 01-Function
## Challenge: Payroll and Tax Calculation System

1. Create a function named 'calculate_salary' that takes two parameters: 'base_hours' and 'hourly_rate'. It must calculate the total gross salary and RETURN the value.
2. Create a second function named 'calculate_tax' that takes 'gross_salary' as a parameter, calculates a 10% tax deduction, and RETURN the tax amount.
3. In the main execution block, use a 'while True' loop to dynamically prompt the operator for the number of days worked, daily shift hours, and hourly rate.
4. Call both functions sequentially, using the output of the first function as the input for the second function.
5. Include robust error handling to ensure all user inputs are numeric, using a 'try-except' block to prevent system crashes.
6. Print a structured receipt showing the Total Hours, Gross Salary, Tax Deduction, and Net Salary (Gross minus Tax) using string formatting.
7. Provide an option to type 'F' at any input prompt to safely shut down the operator console.

# 02-Function
## Challenge: Pricing System

1. Create a function named calculate_final_price that takes two parameters: base_price (the original price of the item) and purchase_hour (an integer from 0 to 23 representing the time of day).
2. If the purchase_hour is between 22 and 23 or between 0 and 4 apply a 15% discount to the base_price.
3. Otherwise (during regular hours), there is no discount, and the price remains the same.
4. The function must RETURN the final price as a clean integer.
5. Call the function twice in your main script to test both scenarios (e.g., a purchase at 2 PM and a purchase at Midnight) and print the results.

# 03-Function
## Challenge: Audio Playlist Duration Analyzer

1. Create a function named 'convert_seconds_to_minutes' that takes one parameter: 'total_seconds'. It must calculate the full minutes and remaining seconds, and RETURN a formatted string using 'f-string' and ':02d' specifier (e.g., M:SS).
2. Create a second function named 'calculate_playlist_duration' that takes 'track_list' (a list of numbers in seconds) as a parameter.
3. Use a 'for' loop to iterate through the 'track_list'. Inside the loop, sequentially call the first function to dynamically print each track's formatted time, add the track's duration to the accumulator, and increment the track number.
4. After the loop completes, call the 'convert_seconds_to_minutes' function one last time, passing the accumulated total seconds to RETURN the aggregated album duration.
5. Call 'convert_seconds_to_minutes' with the total accumulated seconds to RETURN the overall album duration.

# 04-Function
## Challenge: Caesar Cipher Encryptor

1. Create a function named 'encrypt_message' that takes two parameters: 'main_text' and 'key_number'.
2. Inside the function, define a string named 'alphabet' containing all lowercase letters from 'a' to 'z' to serve as your reference roadmap.
3. Use a loop to iterate through each character of the 'main_text' sequentially.
4. For each character, find its corresponding index on the 'alphabet' string, shift this index forward by adding the 'key_number', and extract the new shifted character.
5. Append each newly generated character into a container variable named 'chiper_text' and RETURN the final encrypted message after the loop completes.
6. Print a structured output displaying a security warning message followed by the newly encrypted password using string formatting.

# 05-Function
## Challenge: Patient Heart Rate Analyzer
### Objective:
In medical devices, raw sensor data often contains environmental noise or artifacts (e.g., loose cable connections generating extreme, impossible values). Before analyzing a patient's heart rate metrics, these anomalies must be filtered out to ensure accurate diagnostic calculations. The goal of this challenge is to create a robust signal processing function that filters out extreme noise.

1. Create a function named calculate_signal_energy that takes an arbitrary number of raw heart rate readings using *args and optional keyword arguments using **kwargs.
2. Inside the function, extract the keyword argument max_limit to define the maximum allowable heart rate threshold. If max_limit is not provided by the user, it must default to 100.
3. Use a loop to iterate through all raw samples provided in args.
4. Calculate the final signal energy by computing the sum of squares of the filtered (valid) values only.
5. Print a structured multi-line report showing the Total Samples Received, Valid Samples (Filtered), and the Final Signal Energy using clean string formatting.
