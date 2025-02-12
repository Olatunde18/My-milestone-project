
menu = """Welcome to the Simple Calculator
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
"""

while True:
    print(menu)
    operation = input("Choose an option from the menu: ")
    if operation == "5":
        print("Goodbye")
        break

    elif operation not in ["1", "2", "3", "4"]:
        print("Invalid menu entry, enter a menu number from 1 to 5")
        continue

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    if operation == "1":
        result = first_number + second_number
        print("Result:", result)


    elif operation == "2":
        result = first_number - second_number
        print("Result:", result)


    elif operation == "3":
        result = first_number * second_number
        print("Result:", result)


    elif operation == "4":
        if second_number == 0:
            print("Error: Division by zero is not allowed")

        else:  
            result = first_number / second_number
            print("Result:", result)
