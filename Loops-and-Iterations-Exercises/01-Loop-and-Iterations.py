# Initialize system configuration and credentials
correct_password = "Alireza@1356"
attempts_left = 3

# Main authentication loop
while attempts_left > 0:
    #  Get user input for the password
    user_try = input("Please enter your password:")
    # Validate the password logic
    if user_try == correct_password:
        print("💠Access Granted!✅ \nWelcome to your account.")
        break
    # Decrement the remaining attempts
    else:
        attempts_left -= 1
        # Handle authentication failures and account locking
        if attempts_left > 0:
            print(f"Invalid password!\n💠Remaining attempts: {attempts_left}")
            print("-" * 30)
        else:
            print("💠Access Denied!❌ \nYour account has been locked.")
            
