def solve(cards,numbers):
    finished_cards = []
    winning_number = []
    while cards:
        called_number = numbers.pop(0)
        for i in range(len(cards)):
            for j in range(len(cards[i])):
                for k in range(len(cards[i][j])):
                    if cards[i][j][k] == called_number:
                        cards[i][j][k] = "x"
        for i in range(len(cards)):
            winner = check_for_winner(cards)
            if winner:
                winning_number.append(called_number)
                finished_cards.append(cards.pop(winner-1))
    return get_total(finished_cards[0])*int(winning_number[0]),get_total(finished_cards[-1])*int(winning_number[-1])

def get_total(card):
    total = 0
    for i in range(len(card)):
        card[i] = list(filter(("x").__ne__,card[i]))
        card[i] = list(map(int,card[i]))
        total += sum(card[i])
    return total

def check_for_winner(data):
    for i in range(len(cards)):
        for row in cards[i]:
            if all(item=="x" for item in row):
                return i+1
        cards[i] = transpose(cards[i])
        for row in cards[i]:
            if all(item=="x" for item in row):
                return i+1
    return False

#imagine using numpy lmao
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)
    return matrix_T

with open('4.txt','r') as input:
    data = input.read().splitlines()
numbers = data.pop(0).split(",")
data.pop(0)
for i in range(len(data)):
    data[i] = data[i].split(" ")
    data[i] = list(filter(("").__ne__, data[i]))
data = list(filter(([]).__ne__, data))
cards = []
while data:
    cards.append(data[:5])
    data = data[5:]
sola,solb = solve(cards,numbers)
print(f'part 1 solution is: {sola}')
print(f'part 2 solution is: {solb}')
