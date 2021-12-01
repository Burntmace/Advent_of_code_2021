import numpy as np
def solve(data):
    return sum(list(map(lambda x,y: x>y,data[1:],data)))
with open('input.txt','r') as input:
    data = input.read().splitlines()
print(f'part 1 solution is: {solve(list(map(int,data)))}')
print(f'part 2 solution is: {solve(np.convolve(list(map(int,data)),np.ones(3,dtype=int),"valid"))}')
