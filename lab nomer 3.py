#213 ----------------------
# n = int(input("Enter a number: "))

# for i in range(n):
#     print("#" + " " * i + "#")
#226 ----------------------
# n = int(input("Enter a number: "))
# s = 0

# for i in range(1, n + 1):
#     s += i ** 2

# print(s)

#255----------------------
# def count_three_digit_numbers(n):
#     """
#     Функция для подсчета количества трехзначных чисел,
#     сумма цифр которых равна n.
#     """

#     if n < 1 or n > 27:
#         return 0

#     count = 0
#     for number in range(100, 1000):
#         hundreds = number // 100      
#         tens = (number // 10) % 10  
#         units = number % 10           
#         digit_sum = hundreds + tens + units

#         if digit_sum == n:
#             count += 1

#     return count


# try:
#     n_input = int(input("Введите целое число n: "))
    
#     result = count_three_digit_numbers(n_input)
    
#     print(f"Количество трехзначных чисел с суммой цифр {n_input} равно: {result}")

# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректное целое число.")
#289----------------------
# try:
#     n = int(input("Введіть ціле число n: "))

#     for i in range(1, n + 1):
#         count = 0 
        
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
        
#         output = str(i) + "+" * count
        
#         print(output)

# except ValueError:
#     print("Помилка: потрібно було ввести ціле число.")

#293
try:
    n = int(input("Введіть ціле число n (1 <= n <= 100000): "))

    if not (1 <= n <= 100000):
        print("Помилка: число повинно бути в діапазоні від 1 до 100000.")
    else:
        count = 0
        
        for i in range(1, n + 1):
            
            original_num = i
            reversed_num = 0
            temp = i
            
            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp = temp // 10
            
            if original_num == reversed_num:
                count += 1
        
        print(count)

except ValueError:
    print("Помилка: потрібно було ввести ціле число.")