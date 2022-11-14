# initial variables
board = ""
class TileSet:
	whitePawn = "□ "
	blackPawn = "■ "
	whiteEmpty = "○ "
	blackEmpty = "● "
class Pawn:
	def __init__(self, pos, isKing):
		self.pos = pos
		self.isKing = isKing
whitePawns = []
blackPawns = []
# functions
def coordToIndex(arr): return (8 * arr[1] + arr[0])
def createBoard():
	tempString = ""
	# create empty checkerboard
	for i in range(4):
		for j in range(4): tempString += TileSet.blackEmpty + TileSet.whiteEmpty
		for k in range(4): tempString += TileSet.whiteEmpty + TileSet.blackEmpty
	# create white pawns

	# create black pawns

	return tempString
def printBoard(string):
	print("  0 1 2 3 4 5 6 7")
	for row in range(8):
		print(f"{row} {string[(16 * row):(16 * row + 16)]}")
# function calls
board = createBoard()
printBoard(board)