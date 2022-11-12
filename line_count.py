import os

files = os.listdir()
line_count = 0

for i in files:
    file = open(i, 'r')
    file_line_count = len(file.readlines())
    print(f'{i}: {file_line_count}')
    line_count += file_line_count

with open('line_count.py', 'r') as file:
    main_line_count = len(file.readlines())
    line_count -= main_line_count

print(line_count)