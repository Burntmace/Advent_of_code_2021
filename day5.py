def solve(x1,y1,x2,y2,part):
    dimensions = max(max(x1),max(y1),max(x2),max(y2))
    grid = [[0 for col in range(dimensions+1)] for row in range(dimensions+1)]

    for i in range(len(x1)):
        if x1[i] == x2[i]:
            start = min(y1[i],y2[i])
            for j in range(abs(y1[i]-y2[i])+1):
                grid[start+j][x1[i]] += 1
        elif y1[i] == y2[i]:
            start = min(x1[i],x2[i])
            for j in range(abs(x1[i]-x2[i])+1):
                grid[y1[i]][start+j] += 1
        else:
            if part=="a":
                continue
            startx = min(x1[i],x2[i])
            asc = (y1[i]-y2[i]<0 and startx == x1[i]) or (y2[i]-y1[i]<0 and startx == x2[i])
            for j in range(abs(x1[i]-x2[i])+1):
                if asc:
                    grid[min(y1[i],y2[i])+j][startx+j] += 1
                else:
                    grid[max(y1[i],y2[i])-j][startx+j] += 1

    # displaygrid(grid)
    one_count = sum(x.count(1) for x in grid)
    zero_count = sum(x.count(0) for x in grid)
    count = (dimensions+1)**2 - one_count - zero_count
    return count

def displaygrid(grid):
    for row in grid:
        row = [str(x) for x in row]
        print("".join(row).replace("0",".")+"\n")

with open('5.txt','r') as input:
    data = input.read().splitlines()
x1 = list(map(lambda x : int(x.split(",")[0]),data))
y1 = list(map(lambda x : int(x.split(" ")[0].split(",")[1]),data))
x2 = list(map(lambda x : int(x.split(" ")[2].split(",")[0]),data))
y2 = list(map(lambda x : int(x.split(",")[-1]),data))
print(f'part 1 solution is: {solve(x1,y1,x2,y2,"a")}')
print(f'part 2 solution is: {solve(x1,y1,x2,y2,"b")}')
