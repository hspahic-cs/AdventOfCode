def readInput(filepath):
    with open(filepath) as f:
        input_lines = [line.strip() for line in f]
        return input_lines

def numberTrees(input):
    count = 0
    iteration = 0
    cur_x = -3
    for i in input:
        iteration += 1
        cur_x += 3
        cur_x %= (len(i))

        if i[cur_x] == "#":
            count += 1
            print("Iteration {} : Current X : {}".format(iteration, cur_x))



    return count

def numberTreesProduct(input, x, y):
    count = 0
    iteration = 0
    cur_x = -1 * x
    for i in range(0, len(input), y):
        iteration += 1
        cur_x += x
        cur_x %= (len(input[i]))

        if input[i][cur_x] == "#":
            count += 1


    return count

a = numberTreesProduct(readInput("input2.txt"), 1, 1)
b = numberTreesProduct(readInput("input2.txt"), 3, 1)
c = numberTreesProduct(readInput("input2.txt"), 5, 1)
d = numberTreesProduct(readInput("input2.txt"), 7, 1)
e = numberTreesProduct(readInput("input2.txt"), 1, 2)
print(a*b*c*d*e)
