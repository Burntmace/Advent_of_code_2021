import statistics
def solve(data):
    median = int(statistics.median(data))
    mean = int(statistics.mean(data))
    return sum(abs(x-median) for x in data),sum(sum(range(abs(x-mean)+1)) for x in data)
with open('7.txt','r') as input:
    data = list(map(int,input.read().split(",")))
print(f'part 1 solution is: {solve(data)[0]}')
print(f'part 2 solution is: {solve(data)[1]}')
