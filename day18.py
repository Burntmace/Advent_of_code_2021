import re
def solve(data):
    max_magnitude = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if not i==j:
                max_magnitude = max(max_magnitude,compute_magnitude(reduce("["+data[i]+","+data[j]+"]")))

    while len(data) > 1:
        sum = "["+data[0]+","+data[1]+"]"
        data.pop(0)
        data[0] = reduce(sum)
    return compute_magnitude(data[0]),max_magnitude

def reduce(number):
    reductions_needed = True
    while reductions_needed:
        explosions_needed = True
        while explosions_needed:
            depth = 0
            for i in range(len(number)):
                if i == len(number)-1:
                    explosions_needed = False
                if number[i] == "[":
                    depth += 1
                    if depth == 5:
                        while True:
                            while not number[i].isnumeric():
                                i+=1
                            i-=1
                            pair_index = number[i:].index("]")
                            pair = number[i+1:].split("]")[0]
                            if pair.split(",")[1].isnumeric():
                                break
                            i+=number[i+1:].index("[")
                        left_pair = int(pair.split(",")[0])
                        right_pair = int(pair.split(",")[1])
                        left_number = number[:i]
                        for j in range(len(left_number)-1,-1,-1):
                            if left_number[j].isnumeric():
                                k = j
                                while left_number[k].isnumeric():
                                    k -= 1
                                left_number = left_number[:k+1]+str(int(left_number[k+1:j+1])+left_pair)+left_number[j+1:]
                                break
                        right_number = number[i+pair_index+1:]
                        for j in range(len(right_number)):
                            if right_number[j].isnumeric():
                                k = j
                                while right_number[k].isnumeric():
                                    k += 1
                                right_number = right_number[:j]+str(int(right_number[j:k])+right_pair)+right_number[k:]
                                break
                        number = left_number+"0"+right_number
                        break
                elif number[i] == "]":
                    depth -= 1
        for i in range(len(number)):
            if i == len(number)-1:
                reductions_needed = False
            if number[i].isnumeric() and number[i+1].isnumeric() and not explosions_needed:
                j = i
                while number[j].isnumeric():
                    j += 1
                number = number[:i]+"["+str(int(int(number[i:j])/2))+","+str((int(int(number[i:j])/2) + (int(number[i:j])%2>0)))+"]"+number[j:]
                explosions_needed = True
                break
    return number

def compute_magnitude(data):
    while True:
        roots = re.findall(r'\[[0-9]+\,[0-9]+\]',data)
        for root in roots:
            values = root[1:-1].split(",")
            value = str(int(values[0])*3 + int(values[1])*2)
            data = data.replace(root,value)
            if data.isnumeric():
                return int(data)

with open('18.txt','r') as input:
    data = input.read().splitlines()
solutions = solve(data)
print(f'part 1 solution is: {solutions[0]}')
print(f'part 2 solution is: {solutions[1]}')
