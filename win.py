#hardcoding winning cases (Vertical, Horizontal, Diagonal)

#Win by vertical
game = [[2, 0, 1],
		[2, 0, 1],
		[2, 2, 0],]

#no winner
'''game = [[2, 0, 1],
		[0, 0, 1],
		[2, 2, 0],]'''		

#to detect vertical wins
for col in range(len(game)):
	check = []

	for row in game:
		#print(row[0])
		#append the value that is row 0
		check.append(row[col])

	if check.count(check[0]) == len(row) and check[0] != 0:
		print("Winner!")
#end vertical win
