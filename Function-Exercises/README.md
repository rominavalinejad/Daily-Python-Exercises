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
5. call 'convert_seconds_to_minutes' with the total accumulated seconds to RETURN the overall album duration.
