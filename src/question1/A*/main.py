import NPuzzle

x = NPuzzle.NPuzzle()
x.initialize('8puzzle.txt', 8)
#x.root.grid = [[1,2,3],[4,5,6],[7,0,8]]
#list = x.generate_states(x.root)

print(x.search())
