''''
    Server Port Validator
    This module provides a utility function to validate networking port numbers
    using robust error handling.
'''

def validate_server_port(port_input):
    '''
    Validates if the input port is a valid integer between 1 and 65535.
    Args:
        port_input: The input value to check (can be string or int).
    Returns:
        int: Ok
        str: Error
    '''
    try:
        # Attempt to convert the input into an integer
        port = int(port_input)
        # Check the port number
        if port < 1 or port > 65535:
            return "[Error] Port number out of valid range (1-65535)."
        return port
    except ValueError:
        # Handle the exception if the input contains non-numeric characters
        return "[Error] Port must be a valid integer number."

def main():
    """Run test cases for the server port validator function."""
    # standard port
    user_port_1 = 5257
    print(validate_server_port(user_port_1))

    # out-of-range port number
    user_port_2 = 1900
    print(validate_server_port(user_port_2))

    # out-of-range port number
    user_port_3 = 171980
    print(validate_server_port(user_port_3))

    # out-of-range port number
    user_port_4 = 65539
    print(validate_server_port(user_port_4))

    # standard port
    user_port_5 = 48021
    print(validate_server_port(user_port_5))

if __name__ == "__main__":
    main()
