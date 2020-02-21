import numpy as np
import random as r

def generate_board(board_dimentions, number_of_mines):
	#creates mine feild of dimentions nxm
	board = np.full((board_dimentions[0],board_dimentions[1]),False,dtype=bool)
	mines_placed = 0
	while mines_placed<number_of_mines:
		x=r.randint(0,board_dimentions[0]-1)
		y=r.randint(0,board_dimentions[1]-1)
		if board[x][y]==False:
			board[x][y]==True
			mines_placed+=1
	return board


def generate_adjacency_map(board_dimentions, mine_map):
	#creates an adjacency map for the mines
	board = np.full((board_dimentions[0],board_dimentions[1]),None)
	for i in range(board_dimentions[0]):
		for j in range(board_dimentions[1]):
				if not mine_map[i][j]:
					mines = 0
					for x in [-1,0,1]:
						if i+x>0 or i+x>board_dimentions[0]:
							continue
						for y in [-1,0,1]:
							if j+y>0 or j+y>board_dimentions[1]:
								continue
							if mine_map[i+x][j+y]:
								mines+=1
					board[i][j]=mines
	return board