def solve(data,part):
    xpos = 0
    ypos = 0
    aim = 0
    for line in data:
        if part =="b":
            if line.split(" ")[0] == "forward":
                xpos += int(line.split(" ")[1])
                ypos += int(line.split(" ")[1])*aim
            elif line.split(" ")[0] == "up":
                aim -= int(line.split(" ")[1])
            elif line.split(" ")[0] == "down":
                aim += int(line.split(" ")[1])
        elif part =="a":
            if line.split(" ")[0] == "forward":
                xpos += int(line.split(" ")[1])
            elif line.split(" ")[0] == "up":
                ypos -= int(line.split(" ")[1])
            elif line.split(" ")[0] == "down":
                ypos += int(line.split(" ")[1])
    return(xpos*ypos)

with open('2.txt','r') as input:
    data = input.read().splitlines()
print(f'part 1 solution is: {solve(data,"a")}')
print(f'part 2 solution is: {solve(data,"b")}')
