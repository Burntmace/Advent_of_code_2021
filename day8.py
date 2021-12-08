import string
def parta(data):
    counter = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (len(data[i][j]) == 2) or (len(data[i][j]) == 3) or (len(data[i][j]) == 4) or (len(data[i][j]) == 7):
                counter +=1
    return counter

def partb(data,right_data):
    lights_to_num = {
        119:"0",
        36:"1",
        93:"2",
        109:"3",
        46:"4",
        107:"5",
        123:"6",
        37:"7",
        127:"8",
        111:"9"
    }
    total = 0
    for i in range(len(data)):
        dict = {}
        fives = []
        sixes = []
        for j in range(len(data[i])):
            if len(data[i][j]) == 2:
                dict[36] = data[i][j]
            elif len(data[i][j]) == 3:
                dict[37] = data[i][j]
            elif len(data[i][j]) == 4:
                dict[46] = data[i][j]
            elif len(data[i][j]) == 5:
                fives.append(data[i][j])
            elif len(data[i][j]) == 6:
                sixes.append(data[i][j])
            elif len(data[i][j]) == 7:
                dict[127] = data[i][j]
        fives = get_distinct_chars(fives)
        sixes = get_distinct_chars(sixes)
        dict[1] = "".join([x for x in dict[37] if not x in dict[36]])
        dict[10] = "".join([x for x in dict[46] if not x in dict[36]])
        dict[4] = "".join([x for x in dict[36] if x in sixes])
        dict[8] = "".join([x for x in sixes if x in dict[10]])
        dict[32] = "".join([x for x in dict[36] if x not in dict[4]])
        dict[2] = "".join([x for x in dict[46] if x not in dict[4] and x not in dict[8] and x not in dict[32]])
        dict[16] = "".join([x for x in fives if not x in dict[2] and not x in dict[32] and not x in dict[4]])
        dict[64] = "".join([x for x in dict[127] if not x in dict[46] and not x in dict[16] and not x in dict[1]])

        digits = []
        for k in range(len(right_data[i])):
            sum = 0
            for char in right_data[i][k]:
                sum += list(dict.keys())[list(dict.values()).index(char)]
            digits.append(lights_to_num[sum])
        total += int("".join(digits))
    return total

def get_distinct_chars(lst):
    distinct_list = []
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            d[lst[i][j]] += 1
    for elem in d.keys():
        if not d[elem] == len(lst) and not d[elem] == 0:
            distinct_list.append(elem)
    return distinct_list

with open('8.txt','r') as input:
    data = input.readlines()
    right_data = [x.split("|")[1].split(" ") for x in data]
    right_data = [x for x in right_data if not x == ""]
    left_data = [x.split("|")[0].split(" ") for x in data]
    left_data = [x for x in left_data if not x == ""]
    for i in range(len(right_data)):
        right_data[i][-1] = right_data[i][-1].strip('\n')
        right_data[i].pop(0)
    for i in range(len(left_data)):
        left_data[i].pop(-1)

print(f'part 1 solution is: {parta(right_data)}')
print(f'part 2 solution is: {partb(left_data,right_data)}')
