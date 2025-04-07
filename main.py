def menu():
    print("\n=== Smart Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
def operation(ch,num1,num2):
   if ch == '1':
        return num1 + num2
   elif ch == '2':
        return num1 - num2
   elif ch == '3':
        return num1 * num2
   elif ch == '4':
        if num2 == 0:
            return "Cannot divide by zero!"
        return num1 / num2
   else:
        return "Invalid operation!"


def main():
    while True:
        menu()
        ch = input("Enter your choice (1-5): ").strip()

        if ch == '5':
            print("Exiting Smart Calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result =operation(ch, num1, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numeric input!")


if __name__ == "__main__":
    main()
