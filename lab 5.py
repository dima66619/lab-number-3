#419
# a = input().split()

# res = a[0]
# max_count = 0

# for num in a:
#     count = a.count(num)
#     if count > max_count:
#         max_count = count
#         res = num

# print(res)

#426
# s = input()
# parts = s.split('.')
# print(parts[0], parts[1])

#472
# n = int(input())          
# limit_len = int(input())  
# symbol = input()         

# words = []
# for _ in range(n):
#     words.append(input())

# result = []
# for word in words:
#     if len(word) > limit_len:
#         result.append(word[:-3] + symbol)
#     else:
#         result.append(word)

# print(result)

#474
# n = int(input())

# matrix = [['.' for _ in range(n)] for _ in range(n)]
# center = n // 2

# for i in range(n):
#     matrix[i][i] = '*'           
#     matrix[i][n - 1 - i] = '*'   
#     matrix[center][i] = '*'      
#     matrix[i][center] = '*'      

# for row in matrix:
#     print(*row)

#487
# a = [int(x) for x in input().split()]
# n = len(a)

# if n == 1:
#     print(a[0])
# else:
#     res = []
#     for i in range(n):
#         current_sum = a[i-1] + a[(i+1) % n]
#         res.append(current_sum)
    
#     print(*res)

#496
a = input().split()   
n = input()           

found_positions = []

for i in range(len(a)):
    if a[i] == n:
        found_positions.append(i + 1)

if len(found_positions) > 0:
    print(*found_positions)  
else:
    print("None")