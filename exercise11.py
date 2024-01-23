def reverse_digits(n):
    # Convert the integer to a string to easily iterate over its digits
    num_str = str(n)
    
    # Iterate through each character (digit) in reverse order
    for digit in reversed(num_str):
        print(digit, end=' ')

# Get input from the user
user_input = int(input("Enter an integer: "))

# Call the function to reverse and print the digits
reverse_digits(user_input)

