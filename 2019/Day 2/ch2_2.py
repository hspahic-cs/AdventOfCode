def decoder(filepath, x, y):
    with open(filepath) as f:
        for line in f:
            input = line.split(",")

    input[1] = x
    input[2] = y

    input = list(map(int, input))

    for x in range(0, len(input), 4):
        if input[x] == 1:
            input[input[x + 3]] = input[input[x + 1]] + input[input[x + 2]]
        elif input[x] == 2:
            input[input[x + 3]] = input[input[x + 1]] * input[input[x + 2]]
        else:
            return input[0]
            break

def optimizer(filepath):
    for x in range(99):
        for y in range(99):
            if decoder(filepath, x, y) == 19690720:
                return 100 * x + y

print(optimizer("ch2_2_input.txt"))
