
game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0],]

#function game_board
def  game_board(game_map, player=0, row=0, column=0, just_display=False):

	#try and except for error handling
	try:
		print("   a  b  c")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
				print(count, row)
		return game_map
	#IndexError was the error for when player starts with a row other than possible rows '0', '1', or '2'
	except IndexError as e: 
		print("Error: Make sure you input row/column as '0' '1' or '2'?", e)

	except Exception as e:	
		print("Something went very wrong", e)

game = game_board(game, just_display=True)
game = game_board(game, player=1, row=3, column=1)

