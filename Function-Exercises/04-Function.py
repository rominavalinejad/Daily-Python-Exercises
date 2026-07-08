# ========================
# Caesar Cipher Encryptor
# ========================

def encrypt_message(main_text, key_number):
    '''
    Encrypts a text using the Caesar Cipher algorithm by shifting characters.
    Inputs:
    - main_text (str): The original message to encrypt
    - key_number (int): The number of positions to shift each character
    Returns:
    - str: The encrypted ciphertext
    '''
    # Define the reference line
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chiper_text = ""
    # Loop through each character of the input message
    for char in main_text:
        currect_index = alphabet.find(char)
        # Shift the location forward by the given key number
        new_index = currect_index + key_number
        new_char = alphabet[new_index]
        # Add the new found character
        chiper_text += new_char
    return chiper_text
    
# --> Testing the Function <--
my_pass = "valinejadvnn"
print("\nWarning! This code doesn't offer 100% security,\nso do not share it with anyone!")
print(f"\nYour New Password: {encrypt_message(my_pass, 3)}")
