

# 3x3x3x3 grid of Xs (1s) and Os (-1s) or blank (0s)
Grid = [[[[0 for i in range(3)] for i in range(3)] for i in range(3)] for i in range(3)]

#store move history for each player as 4 indices into grid
Xm = [[-1 for i in range(4)] for i in range(81)] # X moves
Om = [[-1 for i in range(4)] for i in range(81)] # O moves

