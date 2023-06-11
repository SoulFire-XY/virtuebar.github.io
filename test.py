"""
input = [1, 2, 4, 3, 5, 6, 7 , 3, 5 , 2,3, 4]

output = [[1, 2, 4], [5, 6, 7], [5, 2], [4]]
"""

n = ['INT', 'KEYWORD', 'FOR', 'TT_NEWLINE', 'INT', 'STR', 'TT_NEWLINE', 'OP', 'ADD', 'EOF']

def make_line_division( tokens):
		line = []
		TotalProgram = []

		for i in tokens:
			#print(i, type(i))
			#print(True if i == TT_NEWLINE else False)
			if str(i) == 'TT_NEWLINE' or str(i) == 'TT_EOF':
				TotalProgram.append(line)
				line = []
			else:
				line.append(i)
			
		print(line, TotalProgram)

make_line_division(n)

x = ['a', 'b', 'c', 'd', 'b']
sep1 = 'f'
sep2 = 'b'

sep = (sep1, sep2)

for i in x:
	if i in sep:
		print(1)