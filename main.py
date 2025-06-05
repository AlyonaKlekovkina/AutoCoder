import math

def factorial(num):
    # Check if the input is a non-negative integer
    if not isinstance(num, int) or num < 0:
        raise ValueError('Input must be a non-negative integer')
    
    # Calculate the factorial using math module
    result = math.factorial(num)
    return result

if __name__ == '__main__':
    try:
        # Get user input
        num = int(input('Enter a non-negative integer: '))
        
        # Calculate and print the factorial
        print(f'The factorial of {num} is: {factorial(num)}')
    except ValueError as e:
        print(f'Error: {e}')
