def decoder(filepath):
    with open(filepath) as f:
        input_lines = [line.strip() for line in f]
        val1 = 0
        val2 = 0
        for x in input_lines:
            for y in input_lines:
                for z in input_lines:
                    if (int(x) + int(y) + int(z)) == 2020:
                        val1 = int(x)
                        val2 = int(y)
                        val3 = int(z)

        print(val1 * val2 * val3)


decoder("Input2.txt")
