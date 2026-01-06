#314

surname = input()
name = input()
patronymic = input()

print(name[0] + '.' + patronymic[0] + '.' + surname)

#348
n = int(input())

r1 = ""
r2 = ""
r3 = ""
r4 = ""

for i in range(1, n + 1):
    r1 += "+    "
    r2 += "|" + str(i) + " / "
    r3 += "|__\\ " 
    r4 += "|    "

print(r1)
print(r2)
print(r3)
print(r4)

#349
s = input()

space_index = s.find(' ')

word1 = s[:space_index]

word2 = s[space_index + 1:]

print(word2 + ' ' + word1)

#371
s = input()      
char = input()   

count = s.count(char)  

if count == 1:
    print(s.find(char))
elif count > 1:
    print(s.find(char), s.rfind(char))

#399
s = input()

res = ""
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        count += 1
    else:
        if count > 1:
            res += str(count)
        res += s[i]
        count = 1  

if count > 1:
    res += str(count)
res += s[-1]

print(res)

#400
s = input()
clean_s = ""

for char in s:
    if char.isalpha():  
        clean_s += char.lower()  
if clean_s == clean_s[::-1]:
    print("Yes")
else:
    print("No")