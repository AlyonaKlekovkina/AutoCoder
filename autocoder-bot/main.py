import math

def calculate_factorial(num):
    try:
        if num < 0:
            print('Factorial is not defined for negative numbers')
        else:
            result = math.factorial(num)
            return result
    except ValueError:
        print('Invalid input. Please enter a valid integer')

if __name__ == '__main__':
    num = int(input('Enter a number to calculate factorial: '))
    factorial = calculate_factorial(num)
    if factorial:
        print(f'The factorial of {num} is: {factorial}')
