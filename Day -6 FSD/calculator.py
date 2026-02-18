def calculator():
    try:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting calculator...")
            return

        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid choice! Please select 1-5.")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            print("Result:", num1 / num2)

    except ValueError as ve:
        print("Value Error:", ve)

    except ZeroDivisionError as rub:
        print("Math Error:", rub)

    except Exception as e:
        print("Unexpected Error:", e)

    finally:
       
        calculator()

calculator()
