#!/usr/bin/python3
output = ""
for i in range(10):
    for j in range(i + 1, 10):
        output += "{:02d}, {:02d}".format(i, j)
        output += "\n" if i == 8 and j == 9 else ", "
output = output[:179]  
print(output)







