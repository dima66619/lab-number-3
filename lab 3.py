# #number 213
n = int(input())

for i in range(n):
    print('#' + ' ' * i + '#')

#226
n = int(input())

sum_squares = 0

for i in range(1, n + 1):
    sum_squares += i ** 2  

print(sum_squares)

# 255
n = int(input())
count = 0
for i in range(100, 1000):
    if i // 100 + (i // 10) % 10 + i % 10 == n:
        count += 1
print(count)

# 267
n = int(input())

for i in range(n):
    for j in range(n):
        if i == j:
            print(0, end='\t')
        elif i < j:
            print(1, end='\t')
        else:
            print(-1, end='\t')
    print()

# 289
n = int(input())

for i in range(1, n + 1):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            
    print(str(i) + '+' * count)

# 293
n = int(input())

count = 0

for i in range(1, n + 1):
    s = str(i)
    if s == s[::-1]:
        count += 1

print(count)