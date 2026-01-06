#627
# def check_parity(n):
#     if n % 2 == 0:
#         print(True)
#     else:
#         print(False)

# number = int(input())

# check_parity(number)

#628
# def print_even(numbers):
#     res = []
#     for x in numbers:
#         if int(x) % 2 == 0:
#             res.append(x)
#     print(*res)

# data = input().split()

# print_even(data)

#658
# def rainfall_stats(data):
#     months = ["January", "February", "March", "April", "May", "June",
#               "July", "August", "September", "October", "November", "December"]
    
#     total = float(sum(data))
    
#     avg = total / len(data)
    
#     max_val = max(data)
#     min_val = min(data)
    
#     max_month = months[data.index(max_val)]
#     min_month = months[data.index(min_val)]
    
#     return (total, avg, (float(max_val), max_month), (float(min_val), min_month))

# data = [int(x) for x in input().split()]
# print(rainfall_stats(data))

#659
# def is_valid_date(d, m, y):
#     if m < 1 or m > 12:
#         return False
        
#     days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         days[2] = 29
        
#     if d < 1 or d > days[m]:
#         return False
        
#     return True

# d = int(input())
# m = int(input())
# y = int(input())

# print(is_valid_date(d, m, y))

#689
# def is_leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# def get_days_in_month(m, y):
#     if m == 2:
#         return 29 if is_leap(y) else 28
#     elif m in [4, 6, 9, 11]:
#         return 30
#     else:
#         return 31
# def get_next_date(d, m, y):
#     d += 1
#     if d > get_days_in_month(m, y):
#         d = 1
#         m += 1
        
#         if m > 12:
#             m = 1
#             y += 1     
#     return y, m, d
# line = input().split()
# d, m, y = int(line[0]), int(line[1]), int(line[2])
# next_y, next_m, next_d = get_next_date(d, m, y)
# print(f"{next_y}-{next_m}-{next_d}")

#690
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def get_days_in_month(m, y):
    if m == 2:
        return 29 if is_leap(y) else 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31
def get_prev_date(d, m, y):
    d -= 1
    if d == 0:
        m -= 1
        if m == 0:
            m = 12
            y -= 1
        d = get_days_in_month(m, y)
    return y, m, d
line = input().split()
d, m, y = int(line[0]), int(line[1]), int(line[2])
py, pm, pd = get_prev_date(d, m, y)
print(f"{py}-{pm}-{pd}")