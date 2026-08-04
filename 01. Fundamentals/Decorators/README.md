# 01-Decorators
## Challenge: Login Rate Limiter Decorator

1. Build a custom decorator function named rate_limit that takes a target function as its parameter.
2. Initialize an internal execution counter (`attempts`) and utilize the nonlocal keyword to manage its state across function calls.
3. Implement logic inside the inner wrapper function to restrict execution once the maximum limit of 3 attempts is reached.
4. Display system tracking logs for valid attempts and return an [Access Denied] warning message for any excess calls.
