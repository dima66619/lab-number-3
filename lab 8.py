#728
# import math

# print("Input coordinates of two points.")

# x1 = float(input("Starting latitude: "))
# y1 = float(input("Ending longitude: "))

# x2 = float(input("Starting latitude: "))
# y2 = float(input("Ending longitude: "))

# x1_rad = math.radians(x1)
# y1_rad = math.radians(y1)
# x2_rad = math.radians(x2)
# y2_rad = math.radians(y2)

# r = 6371.032

# distance = r * math.acos(math.sin(x1_rad) * math.sin(x2_rad) + 
#                          math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad - y2_rad))

# print(f"The distance is {distance:.2f} km.")

#729
# import math

# n = float(input())

# result = math.modf(n)

# print(result)

#759
# def calculate_file_sum(filename):
#     total = 0
#     with open(filename, 'r') as f:
#         for line in f:
#             if line.strip():  
#                 total += int(line)
#     return total

# fname = input().strip()

# print(calculate_file_sum(fname))

#760
# def calculate_file_average(filename):
#     total_sum = 0
#     count = 0
    
#     with open(filename, 'r') as f:
#         for line in f:
#             if line.strip():
#                 total_sum += float(line)
#                 count += 1
                
#     if count == 0:
#         return 0.0
        
#     return total_sum / count

# fname = input().strip()
# result = calculate_file_average(fname)

# print(f"{result:.2f}")

#790
# def count_votes(filename):
#     candidates = {}
    
#     with open(filename, 'r') as f:
#         for line in f:
#             if line.strip():
#                 parts = line.split()
#                 name = parts[0]
#                 votes = int(parts[1])
                
#                 if name in candidates:
#                     candidates[name] += votes
#                 else:
#                     candidates[name] = votes
#     return candidates

# fname = input().strip()
# results = count_votes(fname)

# for name in sorted(results):
#     print(f"{name} {results[name]}")

#791
def process_sales(filename):
    db = {}
    
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                parts = line.split()
                name = parts[0]
                item = parts[1]
                count = int(parts[2])
                
                if name not in db:
                    db[name] = {}
                    
                if item not in db[name]:
                    db[name][item] = 0
                    
                db[name][item] += count
    return db

fname = input().strip()
sales_data = process_sales(fname)

for name in sorted(sales_data):
    print(f"{name}:")
    
    for item in sorted(sales_data[name]):
        print(f"{item} {sales_data[name][item]}")