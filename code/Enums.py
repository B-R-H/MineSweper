from enum import Enum 

class Flag_state(Enum):
	"""Enumeration for flag states"""
	No_Flag = 0
	Flag = 1
	Maybe = 2

class Game_States(Enum):
	Menu = 0
	Standard_Play = 1
	Flaging = 2
	Game_won = 3
	Game_lost = 4