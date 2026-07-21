'''
Login Rate Limiter Decorator
A decorator to limit the number of execution attempts for a login function.
'''

def rate_limit(f):
    attempts = 0
    def wrapper():
        '''
        Inner wrapper function to track execution count 
        and apply access control logic.
        '''
        nonlocal attempts
        if attempts < 3:
            attempts += 1
            print(f"[System] Attempt {attempts} for 3:")
            f()
        else:
            print("[Access Denied] Too many attempts! Please try again later.")
    return wrapper

@rate_limit
def login():
    '''Simulate a user login function.'''
    print("--- Seccessfully logged in")
    
def main():
    # Execute multiple login calls to test
    login()
    login()
    login()
    login()
    login()
    login()
    
if __name__ == "__main__":
    main()    
