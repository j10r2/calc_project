




x1 = int(input("Введите действительную часть числа 1: "))
y1 = int(input("Введите мнимую часть числа 1 : "))

num1 = complex(x1, y1)

x2 = int(input("Введите действительную часть числа 2: "))
y2 = int(input("Введите мнимую часть числа 2: "))

num2 = complex(x2, y2)
print(num1)
print(num2)

def complex(num1, num2, operand):
    if operand == 1:
        return num1 + num2
    elif operand == 2:
        return num1 - num2
    elif operand == 3:
        return num1 * num2
    elif operand == 4:
        return num1 / num2

print(res)


