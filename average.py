# Function to calculate the average of three numbers
def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Taking input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Calculating the average
average = calculate_average(number1, number2, number3)

# Displaying the result
print("The average of the three numbers is:", average)

