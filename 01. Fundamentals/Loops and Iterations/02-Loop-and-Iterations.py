# ======================================================
# Smart Waste Categorization System - Enterprise Edition
# ======================================================

print("WASTE SORTING System Initialized.\nType <finish> anytime to shut down.")
print("-" *60)

# step 1: System Control & Input Validation
while True:
    # Get dynamic input from the operator
    user_input = input("\nEnter total items to process:").strip()
    # Check for exit condition
    if user_input.lower() == "finish":
        print("\nSystem shutting down safely.")
        break
    # Validation
    if not user_input.isdigit():
        print("Invalid input!❌\nPlease enter a valid number or 'finish'.")
        continue
    # Convert input to integer
    total_items = int(user_input)
    print(f"\nProcessing batch of {total_items} items:")
    print("-" *60)
# step 2: Processing Engine & Logic Execution
    for x in range(1, total_items + 1):
        if (x % 3 == 0) and (x % 5 == 0):
            print(f"🔴 [ID:{x:02d}] Category: E-Waste ----------> [High Priority]")
        elif x % 3 == 0:
            print(f"🟠 [ID:{x:02d}] Category: Plastic Materials ---> [Recyclable]")
        elif x % 5 == 0:
            print(f"🟡 [ID:{x:02d}] Category: Paper & Cardboard ---> [Recyclable]")
        else:
            print(f"♻️ [ID:{x:02d}] Category: Organic Waste ---------> [Standard]")
        print("-" *60)
