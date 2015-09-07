import copy

class State:
	"""
		State of a square
	"""
	def __init__(self,init_state=0):
		""" Don't call this: Use static State.X(), State.O(), State.nil() methods """
		self.state = init_state
	def nil(self):
		return (self.state == 0)
	def X(self):
		return (self.state == 1)
	def O(self):
		return (self.state == 2)
	def __eq__(self,other):
		return (self.state == other.state)

	# Board stuff
	def toState(self):
		return self

	# Move validation stuff
	def move(self,move):
		self.state = move.player.state
	#
	# Static methods
	#
	def nil():
		return State(0)
	def X():
		return State(1)
	def O():
		return State(2)

class Board:
	"""
		State of a board.  This should implement the same interface as the State
		object, so that we can simply recursively nest boards
	"""
	def __init__(self, prototype):
		self.state = [copy.deepcopy(prototype) for i in range(9)]
		self.winner = State.nil()
	def X(self):
		""" Return whether or not X wins """
		return self.winner.X()
	def O(self):
		""" Return whether or not O wins """
		return self.winner.O()
	def nil(self):
		""" Returns if nobody wins: equiv to !O ^ !X """
		return self.winner.nil()
	def __eq__(self,other):
		return (self.X() and other.X()) or
			   (self.O() and other.O()) or
			   (self.nil() and other.nil())

	def toState(self):
		if self.O():
			return State.O()
		elif self.X():
			return State.X()
		else:
			return State.nil()

	def move(self,move):
		# TODO: Validate move
		# Update board state
		position = move.moves[0]
		move.moves.pop(0)
		self.state[position[0]*3+position[1]].move(move)
		# Check for winners
		self.winner = move.player if self.__checkWinner(move.player)

	def __checkWinner(self,state):
		# Check if 'state' is in a winning position
		# Scan columns and rows
		for ix1 in range(3):
			row_same == True
			col_same == True
			for ix2 in range(3):
				row_same = row_same and (self.state[ix2*3+ix1] == state)
				col_same = col_same and (self.state[ix1*3+ix2] == state)
			if (row_same or col_same):
				return True
		# Scan diagonals
		right_diag == True
		left_diag  == True
		for ii in range(3):
			right_diag = right_diag and (self.state[ii*4] == state)
			left_diag  = left_diag and (self.state[ii*2 + 2] == state)
		if (left_diag or right_diag):
			return  True
		return False

def Move:
	def __init__(self,bigsquare,smallsquare,player_state):
		self.moves  = [bigsquare smallsquare]
		self.player = player_state

def Game:
	def __init__(self,player1,player2):
		self.players = [player1, player2] # X then O
		self.cur_player = 0
		self.board = Board(Board(State.nil()))

	def playMove(self):
		move = self.players[currentPlayer].getMove(self.board)
		# Parse out Move object and pass to Board
		self.cur_player = (self.cur_player + 1) % 2
		return self.board.toState()

	def gameLoop(self):
		gameState = State.nil()
		while (gameState.nil()):
			gameState = self.playMove()
		return gameState
