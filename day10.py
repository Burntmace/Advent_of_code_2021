def solve(data):
    score = 0
    score2 = []
    point_values = {
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
    }
    for line in data:
        opens = []
        for i in range(len(line)):
            if line[i] in ["(","[","{","<"]:
                opens.append(line[i])
            else:
                isvalid = check_validity(opens[-1],line[i])
                if not isvalid:
                    score += point_values[line[i]]
                    break
                else:
                    opens.pop(-1)
        if isvalid:
            score2.append(calculate_score(opens))
    score2.sort()
    return score, score2[int(len(score2)/2)]

def calculate_score(lst,score=0):
    point_values = {
        "(":1,
        "[":2,
        "{":3,
        "<":4
    }
    if lst == []:
        return score
    x = lst.pop(-1)
    return calculate_score(lst,score*5+point_values[x])

def check_validity(x,y):
    return any([(x=="(" and y==")"),(x=="[" and y=="]"),(x=="{" and y=="}"),(x=="<" and y==">")])

with open('10.txt','r') as input:
    data = input.read().splitlines()
print(f'part 1 solution is: {solve(data)[0]}')
print(f'part 2 solution is: {solve(data)[1]}')
