# #task 112
# sashko_age = int(input("Введіть вік Сашка: "))
# tatyana_age = int(input("Введіть вік Тетянки: "))

# if sashko_age > tatyana_age:
#     print("Sashko is the eldest.")
# elif tatyana_age > sashko_age:
#     print("Tatyana is the eldest.")
# else:
#     print("Sashko and Tatyana are the same age.")
# #task 137
# number = int(input("Введіть натуральне число: "))

# if number % 10 == 5:
#     print("Число закінчується на 5.")
# else:
#     print("Число не закінчується на 5.")
# #task 162
# banknotes = {
#     1: "Володимир Великий",
#     2: "Ярослав Мудрий",
#     5: "Богдан Хмельницький",
#     10: "Іван Мазепа",
#     20: "Іван Франко",
#     50: "Михайло Грушевський",
#     100: "Тарас Шевченко",
#     200: "Леся Українка",
#     500: "Григорій Сковорода",
#     1000: "Володимир Вернадський"
# }

# try:
#     denomination = int(input("Введіть номінал банкноти: "))
#     person = banknotes.get(denomination)

#     if person:
#         print(f"{denomination} гривень - {person}")
#     else:
#         print(f"Банкноти номіналом {denomination} гривень не існує.")
# except ValueError:
#     print("Будь ласка, введіть номінал числом.")
# #task 167
# try:
#     number = int(input("Введіть натуральне число: "))
#     if (number >= 10 and number <= 99):
#         print("Число є двозначним.")
#     elif (number >= 100 or number <= 10):
#         print("Число не э двозначним.")
# except ValueError:
#     print("Помилка: введіть, будь ласка, число.")
# #task 181
# try:
#     number = int(input("Введіть десяткове число: "))

#     binary_representation = bin(number)
#     binary_string = binary_representation[2:]
#     byte_string = binary_string.zfill(8)
    
#     is_palindrome = (byte_string == byte_string[::-1])
    
#     print(is_palindrome)

# except ValueError:
#     print("Помилка: введіть, будь ласка, ціле число.")
# #task 190
# try:
#     a = int(input("Введіть перше число: "))
#     b = int(input("Введіть друге число: "))
#     c = int(input("Введіть третє число: "))

#     if a >= b and a >= c:
#         maximum = a
#         if b >= c:
#             middle = b
#             minimum = c
#         else:
#             middle = c
#             minimum = b
#     elif b >= a and b >= c:
#         maximum = b
#         if a >= c:
#             middle = a
#             minimum = c
#         else:
#             middle = c
#             minimum = a
#     else:
#         maximum = c
#         if a >= b:
#             middle = a
#             minimum = b
#         else:
#             middle = b
#             minimum = a
            
#     print(maximum)
#     print(minimum)
#     print(middle)

# except ValueError:
#     print("Помилка: введіть, будь ласка, ціле число.")