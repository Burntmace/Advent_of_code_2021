def solve(data):
    risk = 0
    basins = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            check_vertical = [x for x in [i-1,i+1] if x>=0 and x<len(data)]
            check_horizontal = [x for x in [j-1,j+1] if x>=0 and x<len(data[i])]
            lowpoint = all([data[i][j] < data[x][j] for x in check_vertical]) and all([data[i][j] < data[i][x] for x in check_horizontal])
            if lowpoint:
                risk+= 1+data[i][j]
                basins.append([(i,j)])
    basins = list(map(len,fill_basins(basins,data)))
    basins.sort()
    return risk,basins[-1]*basins[-2]*basins[-3]

def fill_basins(basins,data):
    for i in range(len(basins)):
        points_to_check = basins[i].copy()
        while points_to_check:
            n,m = points_to_check[0][0],points_to_check[0][1]
            points_to_check.pop(0)
            check_vertical = [x for x in [n-1,n+1] if x>=0 and x<len(data)]
            check_horizontal = [x for x in [m-1,m+1] if x>=0 and x<len(data[0])]
            for x in check_vertical:
                if not (x,m) in basins[i] and not data[x][m] == 9:
                    basins[i].append((x,m))
                    points_to_check.append((x,m))
            for x in check_horizontal:
                if not (n,x) in basins[i] and not data[n][x] == 9:
                    basins[i].append((n,x))
                    points_to_check.append((n,x))
    return basins

with open('9.txt','r') as input:
    data = input.read().splitlines()
data = [list(map(int,list(x))) for x in data]
solve(data)
print(f'part 1 solution is: {solve(data)[0]}')
print(f'part 2 solution is: {solve(data)[1]}')
