#was very tired doing this so I just implemented the most naive thing
#runs in like 30 seconds. To optimise you'd want to work just on the input tuples
#instead of converting to an actual grid, do the grid at the end.
def solve(data,folds,num_folds,show_grid):
    grid = create_grid(data)
    for n in range(num_folds):
        instruction = folds.pop(0)
        fold_direction = instruction[0]
        fold_index = int(instruction.split("=")[1])
        if fold_direction == "x":
            grid = transpose_grid(grid)
            second_half = grid[fold_index:]
            second_half.reverse()
            grid = grid[:fold_index]
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if second_half[i][j]:
                        grid[i][j] = 1
            grid = transpose_grid(grid)
        if fold_direction == "y":
            second_half = grid[fold_index:]
            second_half.reverse()
            grid = grid[:fold_index]
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if second_half[i][j]:
                        grid[i][j] = 1

    if show_grid:
        print_grid(grid)
        return ""
    else:
        return sum(sum(grid,[]))

def transpose_grid(grid):
    xdim = len(grid)
    ydim = len(grid[0])

    transposed_grid = []
    for j in range(ydim):
        transposed_row = []
        for i in range(xdim):
            transposed_row.append(grid[i][j])
        transposed_grid.append(transposed_row)
    return transposed_grid

def create_grid(data):
    xdim = max([int(x.split(",")[0]) for x in data])+1
    ydim = max([int(x.split(",")[1]) for x in data])+1
    grid = [[0 for x in range(xdim)] for y in range(ydim)]
    for x in range(xdim):
        for y in range(ydim):
            if str(x)+","+str(y) in data:
                grid[y][x] = 1
    return grid

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                grid[i][j] = "█"
            else:
                grid[i][j] = " "
    for row in grid:
        print("".join(row))
    return

with open('13.txt','r') as input:
    data = input.read().splitlines()
i = data.index("")
folds = [x.split(" ")[-1] for x in data[i+1:]]
data = data[:i]
print(f'part 1 solution is: {solve(data,folds,1,False)}')
print(f'part 2 solution is the above image {solve(data,folds,len(folds),True)}')
