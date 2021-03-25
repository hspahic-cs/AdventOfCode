def readInput(filepath):
    with open(filepath) as f:
        input_lines = [line.strip() for line in f]
        return input_lines

def passwordChecker(input):
    count = 0
    for line in input:
        x = line.split(' ')
        range = x[0].split('-')
        print(x)
        print(range)

        if int(range[0]) <= x[2].count(x[1][0]) and int(range[1]) >= x[2].count(x[1][0]):
            count+=1
    return count

def passwordCheckerPart2(input):
    count = 0
    for line in input:
        x = line.split(' ')
        range = x[0].split('-')
        print(x)
        print(range)
        bool1 = x[2][int(range[0]) - 1] == x[1][0]
        bool2 = x[2][int(range[1]) - 1] == x[1][0]
        if bool1 != bool2:
            count+=1
    return count

print(passwordCheckerPart2(readInput("input2.txt")))
