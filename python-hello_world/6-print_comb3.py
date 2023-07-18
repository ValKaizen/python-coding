#!/usr/bin/python3
char_limit = 179
char_count = 0

for i in range(1, 10):
    for j in range(i + 1, 10):
        combination = "{:02d}, {:02d}".format(i, j)
        char_count += len(combination)

        if char_count <= char_limit:
            print(combination)
        else:
            break
    else:
        continue
    break
print()