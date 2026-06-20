try:
    num1,num2=eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("The result is", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
except SyntaxError:
    print("Error: Invalid input format. Please enter two numbers separated by a comma.")
finally:
    print("Finally block executed.")