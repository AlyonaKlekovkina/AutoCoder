import math

# Function to calculate factorial

def factorial(n):
    if n < 0:
        return 'Factorial is not defined for negative numbers'
    elif n == 0:
        return 1
    else:
        return math.factorial(n)

# Main function to take user input and call factorial function

def main():
    try:
        num = int(input('Enter a number to calculate factorial: '))
        result = factorial(num)
        print(f'Factorial of {num} is {result}')
    except ValueError:
        print('Please enter a valid integer')
    except Exception as e:
        print('An error occurred:', e)

if __name__ == '__main__':
    main()
