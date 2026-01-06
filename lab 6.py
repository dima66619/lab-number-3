#526
# data = {
#     "JavaSript": "Brendan Eich",
#     "Python": "Guido van Rossum",
#     "Ruby": "Yukihiro Matsumoto",
#     "PHP": "Rasmus Lerdorf"
# }

# for lang, creator in data.items():
#     print(f"My favorite programming language is {lang}. It was created by {creator}.")

#527
# morse_code = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..'
# }

# letter = input()
# print(morse_code[letter.upper()])

#558
# n = int(input())
# synonyms = {}

# for i in range(n):
#     w1, w2 = input().split()
    
#     synonyms[w1] = w2
#     synonyms[w2] = w1

# target_word = input()
# print(synonyms[target_word])

#559
# data = input().split()
# counts = {}
# for i in range(1, 10):
#     counts[str(i)] = 0

# for num in data:
#     if num == '0':
#         break  
    
#     if num in counts:
#         counts[num] += 1

# result_values = []
# for i in range(1, 10):
#     result_values.append(counts[str(i)])
# print(*result_values)

#590
# pos = input()

# c = ord(pos[0]) - ord('a')
# r = 8 - int(pos[1])

# board = [['.' for _ in range(8)] for _ in range(8)]
# board[r][c] = 'K'

# moves = [
#     (-2, -1), (-2, 1), (-1, -2), (-1, 2),
#     (1, -2), (1, 2), (2, -1), (2, 1)
# ]

# for dr, dc in moves:
#     nr, nc = r + dr, c + dc
#     if 0 <= nr < 8 and 0 <= nc < 8:
#         board[nr][nc] = '*'

# for row in board:
#     print(*row)

#591
pos = input()

qc = ord(pos[0]) - ord('a')
qr = 8 - int(pos[1])

board = [['.' for _ in range(8)] for _ in range(8)]

for r in range(8):
    for c in range(8):
        if r == qr and c == qc:
            board[r][c] = 'Q'
        elif r == qr or c == qc or abs(r - qr) == abs(c - qc):
            board[r][c] = '*'

for row in board:
    print(*row)