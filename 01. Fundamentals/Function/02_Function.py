def calculate_final_price(base_price, purchase_hours):
    '''
    Calculate the final price of an item based on the purchase hour.
    + Applies a 15% discount for late-night shopping (22-23 and 0-4).
    
    '''
    # Check if the purchase time is during the late-night discount hours
    if (22 <= purchase_hours <= 23) or (0 <= purchase_hours <= 4):
        price_off = base_price * 0.15
        low_price = base_price - price_off
        final_price = low_price
    else:
        # No discount during regular hours
        final_price = base_price
    # Return the final price as a clean int
    return int(final_price)

#  --- Test Cases ---

# Test 1: Regular hours (11 AM) -> Should return 10
print(calculate_final_price(10, 11))
# Test 2: Discount hours (11 PM) -> Should return 8
print(calculate_final_price(10, 23))
