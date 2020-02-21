import numpy as np
import initlization_functions as IF
import Enums

class board:
	"""Class to hold the mine map adgacency map and shown map"""
	def __init__(self, feild_dimentions, number_of_mines):
		self.mine_map = generate_board(board_dimentions, number_of_mines)
		self.adjancy_map = generate_adjacency_map(board_dimentions, mine_map)
		self.visibility_map = np.full((board_dimentions[0],board_dimentions[1]),False,dtype=bool)
		self.flaged_map = np.full((board_dimentions[0],board_dimentions[1]),0,dtype=int)

def update_visibility(cordinate):
	#update the visibility matrix using recursion
	if self.mine_map[cordinate[0]][cordinate[1]]:
		#update_game_state(Lose)
	elif self.adjancy_map!=0:
		self.visibility_map[cordinate[0]][cordinate[1]]=True
	else:
		self.visibility_map[cordinate[0]][cordinate[1]]=True
		for i in range(len(self.visibility_map)):
			for j in range(len(self.visibility_map[0])):
					if not self.visibility_map[i][j]:
						for x in [-1,0,1]:
							if i+x>0 or i+x>len(self.visibility_map):
								continue
							for y in [-1,0,1]:
								if j+y>0 or j+y>len(self.visibility_map[0]):
									continue
								if self.adjancy_map[i+x][j+y]==0:
									self.update_visibility([i+x,j+y])