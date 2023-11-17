input_string = "Guvi Geeks Network Private Limited"

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count_A = 0
count_E = 0
count_I = 0
count_O = 0
count_U = 0

for char in input_string:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1
    elif char == 'A':
        count_A += 1
    elif char == 'E':
        count_E += 1
    elif char == 'I':
        count_I += 1
    elif char == 'O':
        count_O += 1
    elif char == 'U':
        count_U += 1

total_vowels = count_a + count_e + count_i + count_o + count_u + count_A + count_E + count_I + count_O + count_U

print("Total number of vowels:", total_vowels)
print("Count of each individual vowel:")
print("a:", count_a)
print("e:", count_e)
print("i:", count_i)
print("o:", count_o)
print("u:", count_u)
print("A:", count_A)
print("E:", count_E)
print("I:", count_I)
print("O:", count_O)
print("U:", count_U)


