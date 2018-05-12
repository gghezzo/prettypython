# The 8 Queen Problem  (note: also add the guess the numbert  )
# From https://wiki.python.org/moin/SimplePrograms
# Typer: Ginny C Ghezzo 
# What I learned:   

board_size = int(input("What board size: '" ))
def under_attack(col, queens):
	left = right = col 
	for r, c in reversed(queens):
		left, right = left -1, right + 1
		if c in (left, col, right):
			return True
	return False

def solve(n):
	if n == 0:
		return[[]]
	smaller_solutions = solve(n-1)
	return[solution+[(n,i+1)]
		for i in range(board_size)
			for solution in smaller_solutions
				if not under_attack(i+1, solution)]

x = 1
for answer in solve(board_size):
	print("Answer ",x, answer) 
	x +=1

