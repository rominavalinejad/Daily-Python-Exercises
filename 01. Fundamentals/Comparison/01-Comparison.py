# Check number conditions
print("=" * 35)
print("Welcome to the Chained Comparison!")
print("=" * 35)

# Get three numbers from the user and convert them to int
a = int(input("Enter number a - first int: "))
b = int(input("Enter number b - second int: "))
c = int(input("Enter number c - third int: "))

# Chained Comparison Logic (want: a <= b <= c)
bool_result = a <= b <= c

# Print the boolean result nicely (True or False)
print("-"*15)
print(f"Result: {bool_result}")
print("-"*15)

# Conditional Analysis
if bool_result:
    print("STATUS: The numbers are perfectly sorted in ascending order!")
else:
    print("STATUS: The numbers are NOT sorted in ascending order.")
