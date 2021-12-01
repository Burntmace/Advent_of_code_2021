def solve(data,offset):
    return sum(list(map(lambda x,y: x>y,data[offset:],data)))
with open('input.txt','r') as input:
    data = input.read().splitlines()
print(f'part 1 solution is: {solve(list(map(int,data)),1)}')
print(f'part 2 solution is: {solve(list(map(int,data)),3)}')
