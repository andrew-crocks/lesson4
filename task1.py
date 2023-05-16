while True:
    num1 = input("Введіть перше число (або 'quit' для виходу): ")
    if num1 == "quit":
        break

    operator = input("Введіть математичний оператор (+, -, *, /): ")
    if operator == "quit":
        break

    num2 = input("Введіть друге число (або 'quit' для виходу): ")
    if num2 == "quit":
        break

    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Ошыбка: нельзя делить на ноль ")
            continue 
        result = num1 / num2
    else:
        print("неподдерживаемый оператор")
        continue 

    print("Результат: ", result)
    
    