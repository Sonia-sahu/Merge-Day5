# Prompt the user to enter the first number
num1_str = input("Enter the first number: ")

# Prompt the user to enter the second number
num2_str = input("Enter the second number: ")

# Convert the input strings to floating-point numbers
# Using float() allows for both integer and decimal inputs
num1 = float(num1_str)
num2 = float(num2_str)

# Calculate the sum
sum_result = num1 + num2

# Display the result to the user
print(f"The sum of {num1} and {num2} is: {sum_result}")
