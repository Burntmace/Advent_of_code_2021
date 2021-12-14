def solve(chain,dict,its):
    new_chain = {}
    counting_dict = {}
    for i in range(len(chain)):
        if chain[i] in counting_dict.keys():
            counting_dict[chain[i]] += 1
        else:
            counting_dict[chain[i]] = 1
    for i in range(len(chain)-1):
        if chain[i:i+2] in new_chain.keys():
            new_chain[chain[i:i+2]] += 1
        else:
            new_chain[chain[i:i+2]] = 1
    chain = new_chain
    for n in range(its):
        new_chain = {}
        for elem in chain.keys():
            counter = chain[elem]
            product = dict[elem]
            if product in counting_dict.keys():
                counting_dict[product] += counter
            else:
                counting_dict[product] = counter
            new_polymers = [elem[0]+product,product+elem[1]]
            for polymer in new_polymers:
                if polymer in new_chain.keys():
                    new_chain[polymer] += counter
                else:
                    new_chain[polymer] = counter
        chain = new_chain

    return max(counting_dict.values()) - min(counting_dict.values())
with open('14.txt','r') as input:
    data = input.read().splitlines()
chain = data[0]
reactions = data[2:]
dict = {}
for reaction in reactions:
    dict[reaction.split(" ")[0]] = reaction.split(" ")[-1]
print(f'part 1 solution is: {solve(chain,dict,10)}')
print(f'part 2 solution is: {solve(chain,dict,40)}')
