def solve(data,part):
    maximum = max(data)
    totals= []
    for i in range(maximum):
        total = 0
        for j in range(len(data)):
            if part=="a":
                total += abs(data[j]-i)
            else:
                total += sum(range(abs(data[j]-i)+1))
        totals.append(total)
    return min(totals)
with open('7.txt','r') as input:
    data = list(map(int,input.read().split(",")))
print(f'part 1 solution is: {solve(data,"a")}')
print(f'part 2 solution is: {solve(data,"b")}')
