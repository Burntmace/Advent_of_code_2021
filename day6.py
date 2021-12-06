def solve(data,numdays):
    age = [0]*9
    for fish in data:
        age[fish] += 1
    for day in range(numdays):
        age[(day+7)%9] += age[day%9]
    return sum(age)
with open('6.txt','r') as input:
    data = list(map(int,input.read().split(",")))
print(f'part 1 solution is: {solve(data,80)}')
print(f'part 2 solution is: {solve(data,256)}')
