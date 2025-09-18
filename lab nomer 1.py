#task 11
a11 = int(input("Введите число: "))

b11 = a11 // 10
print("Десятки:", b11)
#task 36
a36 = int(input("Введите 1 число: "))
b36 = int(input("Введите 2 число: "))
c36 = a36/b36
d36 = b36/a36
print(f"{c36:9.5f}***{d36:9.5f}")
#task 6
a6 = int(input("Введите число: "))
b6 = a6 % 10
print(b6)
#task 57
a57 = float(input("Введите массу пирога в кг: "))
b57 = a57/100*28
c57 = b57*1000
print(c57, " грамм масса борошна")
#task 66
n66 = int(input("Введите число: "))
k66 = int(input("Введите количество цифр сколько нужно отрезать от конца "))
a66 = n66 // 10**k66
print(a66)
#task 89
a89 = int(input("Введите 1 число: "))
b89 = int(input("Введите 2 число: "))
с89 = int(input("Введите 3 число: "))
min89 = min(a89, b89, с89)
max89 = max(a89, b89, с89)
mid89 = a89 + b89 + с89 - min89 - max89
print(min89, mid89, max89, sep="\n")