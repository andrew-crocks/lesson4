age =int(input('Введите возраст: '))


if age < 2:
    print("baby")
elif 2 <= age < 4:
    print("kid")
elif 4 <= age < 13:
    print("child")
elif 13 <= age < 20:
    print("teenager")
elif 20 <= age < 65:
    print("grown-up")
else:
    print("senior")