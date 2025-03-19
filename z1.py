num = input("Введіть трицифрове число: ")

if not num.isdigit() or len(num) != 3:
    print("Помилка: введіть саме трицифрове число")
else:
    num = int(num)
    first_digit = num // 100
    last_digit = num % 10
    
    if first_digit == last_digit:
        print("Число є паліндромом")
    else:
        print("Число не є паліндромом")
