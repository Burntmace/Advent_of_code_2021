#encountered some weird edge case bug, and the code I inserted to fix it is kinda messy, but it works so won't fix.
def solve(data,restep_allowed,current_location="start",previous_location="",already_visited_small_caves=[]):
    counter = 0
    if previous_location.islower() and not restep_allowed:
        data = list(filter(lambda x:previous_location not in x,data))
    elif previous_location.islower() and restep_allowed:
        already_visited_small_caves.append(previous_location)
    if current_location == "end":
        return 1
    possible_paths = list(filter(lambda x:current_location in x,data))
    if possible_paths == []:
        return 0
    for path in possible_paths:
        next_location = [x for x in path if not x == current_location][0]
        if next_location == "start":
            continue
        if next_location in already_visited_small_caves and not restep_allowed:
            continue
        if next_location in already_visited_small_caves:
            counter += solve(data,False,next_location,current_location,already_visited_small_caves.copy())
        else:
            counter += solve(data.copy(),restep_allowed,next_location,current_location,already_visited_small_caves.copy())
    return counter

with open('12.txt','r') as input:
    data = input.read().splitlines()
data = list(map(lambda x: (x.split("-")[0],x.split("-")[1]),data))
print(f'part 1 solution is: {solve(data,False)}')
print(f'part 2 solution is: {solve(data,True)}')
