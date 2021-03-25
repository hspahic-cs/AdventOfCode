def decoder(filepath):
    with open(filepath) as f:
        for line in f:
            input = line.split(",")

    input[1] = 12
    input[2] = 2

    input = list(map(int, input))

    for x in range(0, len(input), 4):
        if input[x] == 1:
            input[input[x + 3]] = input[input[x + 1]] + input[input[x + 2]]
        elif input[x] == 2:
            input[input[x + 3]] = input[input[x + 1]] * input[input[x + 2]]
        else:
            print(input)
            break

decoder("ch1_2_input.txt")
