num_levels = 5

num = 1

for i in range(1, num_levels + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()