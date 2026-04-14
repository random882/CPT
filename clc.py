
while True:
    a = float(input("Give me the first number: "))
    b = float(input("Give me the second number: "))
    symbol = input("What would you like to do? (+ - * /): ")

    if symbol == "+":
        result = a + b
    elif symbol == "-":
        result = a - b
    elif symbol == "*":
        result = a * b
    elif symbol == "/":
        if b == 0:
            print("Cannot divide by 0")
            continue
        result = a / b
    else:
        print("Not a valid request")
        continue

    print(f"{a} {symbol} {b} = {result}")

    again = input("Would you still like to try again? (y/n): ")
    if again != "y":
        break