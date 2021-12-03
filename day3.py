def solveb(data,type):
    maxbit = 2**len(data[0])
    epsilon = maxbit
    intdata = [int(x,2) for x in data]
    oxygen = ''
    while len(data) > 1:
        intdata = [x-(maxbit/2) for x in intdata]
        counter = sum(map(lambda x: x>=0,intdata))
        maxbit = maxbit/2
        if counter >= len(data)/2:
            dropbit = str(type)
        else:
            dropbit = str(abs(type-1))
        oxygen += dropbit
        if not type == 2:
            data = [x[1:] for x in data if x[0] == dropbit]
        else:
            data = [x[1:] for x in data]
        data = [x for x in data if not x == '']
        intdata = [int(x,2) for x in data]
    if not type == 2:
        if data:
            oxygen += data[0]
    else:
        oxygen = ''.join(map(str,[int(x)-1 for x in oxygen]))
        oxygen = int(oxygen,2)
        oxygen = oxygen*(epsilon-(oxygen+1))
        return oxygen
    return(int(oxygen,2))

with open('3test.txt','r') as input:
    data = input.read().splitlines()
print(f'part 1 solution is: {solveb(data,2)}')
print(f'part 2 solution is: {solveb(data,1)*solveb(data,0)}')
