from random import choice


class mazeCell:
    def __init__(self, position):
        self.position = position
        self.next = None
        self.direction = None
        self.visited = False

def generateMaze(size):
    maze = []
    mazeUnvisited = []
    if size%2 == 0: size += 1 #size must be odd
    for i in range(size):
        maze.append([]) #the maze is a nxn nested set
        for j in range(size):
            newCell = mazeCell((i, j))
            maze[i].append(newCell)
            mazeUnvisited.append(newCell) #list of unvisited maze cells

    VisitedCell = choice(choice(maze))
    VisitedCell.visited = True      #marking a random cell of the maze as visited
    mazeUnvisited.remove(VisitedCell)

    while (mazeUnvisited):
        CurrentCell = choice(mazeUnvisited)
        FirstCell = CurrentCell
        while CurrentCell.visited is False:
            xy = CurrentCell.position
            dir = choice([(0, 1), (0, -1), (1, 0), (-1, 0)]) #randomly choose next adjacent cell
            while not (tuple(map(sum, zip(xy, dir))) >= (0, 0) and tuple(map(sum, zip(xy, dir)))[0] < len(maze) and
                       tuple(map(sum, zip(xy, dir)))[1] < len(maze)): #check bounds real dirty
                dir = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            i, j = tuple(map(sum, zip(xy, dir)))
            CurrentCell.next = (i, j)
            CurrentCell.direction = dir
            CurrentCell = maze[i][j]

        CurrentCell = FirstCell
        while CurrentCell.visited is False:
            CurrentCell.visited = True
            mazeUnvisited.remove(CurrentCell)
            CurrentCell = maze[CurrentCell.next[0]][CurrentCell.next[1]]
    return maze



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maze = generateMaze(8)
    for cells in maze:
        print("\n")
        for cell in cells:
            print(f"{cell.direction}",end=" | ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
