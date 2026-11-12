import math  # Import math module

# Ask the user for a number
try:
    num = float(input("Enter a non-negative number: "))

    # Check if number is valid
    if num < 0:
        print("Error: Please enter a non-negative number.")
    else:
        # Calculate square root
        result = math.sqrt(num)
        print(f"Square root of {num} is {result}")
except ValueError:
    print("Error: Please enter a valid number.")