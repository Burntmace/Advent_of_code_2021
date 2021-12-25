def solve(data):
    shortest_path_cost = 0
    current_node = (0,0)
    visited_nodes = set()
    unvisited_nodes = [(x,y) for x in range(len(data[0])) for y in range(len(data))]
    distances = [[-1 for x in range(len(data[0]))] for y in range(len(data))]
    distances[0][0] = 0
    while unvisited_nodes:
        nodes_to_check = get_neighbours(current_node,data,visited_nodes)
        for i in range(len(nodes_to_check)):
            if nodes_to_check[i] in visited_nodes:
                continue
            if distances[current_node[0]][current_node[1]] + data[nodes_to_check[i][0]][nodes_to_check[i][1]] < distances[nodes_to_check[i][0]][nodes_to_check[i][1]] or distances[nodes_to_check[i][0]][nodes_to_check[i][1]] == -1:
                distances[nodes_to_check[i][0]][nodes_to_check[i][1]] = distances[current_node[0]][current_node[1]] + data[nodes_to_check[i][0]][nodes_to_check[i][1]]
        visited_nodes.add(current_node)
        unvisited_nodes.remove(current_node)

        minvalue = None
        for n in range(len(distances[0])):
            for m in range(len(distances)):
                if (minvalue == None or distances[n][m] < minvalue) and not distances[n][m] == -1 and not (n,m) in visited_nodes:
                    minvalue = distances[n][m]
                    current_node = (n,m)
    return distances[-1][-1]

def expand_data(data):
    expanded_data = []
    row_num = 0
    for row in data:
        expanded_data.append([])
        for i in range(5):
            expanded_data[row_num] += [x+i for x in row]
        for i in range(len(expanded_data[row_num])):
            if expanded_data[row_num][i] > 9:
                expanded_data[row_num][i] -= 9
        row_num += 1
    temp_thing = expanded_data.copy()
    for j in range(4):
        for row in temp_thing:
            temp = [x+j+1 for x in row]
            for i in range(len(temp)):
                if temp[i] > 9:
                    temp[i] -= 9
            expanded_data.append(temp)
    return expanded_data

def get_neighbours(node,data,visited_nodes):
    vertical = [x for x in [node[1]-1,node[1]+1] if x>=0 and x<len(data)]
    vertical_neighbours = [(node[0],x) for x in vertical]
    horizontal = [x for x in [node[0]-1,node[0]+1] if x>=0 and x<len(data[0])]
    horizontal_neighbours = [(x,node[1]) for x in horizontal]
    return vertical_neighbours+horizontal_neighbours


with open('15.txt','r') as input:
    data = input.read().splitlines()
data = [[int(x) for x in data[y]]for y in range(len(data))]

print(f'part 1 solution is: {solve(data)}')
print(f'part 2 solution is: {solve(expand_data(data))}')
