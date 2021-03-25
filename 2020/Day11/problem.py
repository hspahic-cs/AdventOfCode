import copy

def split(word):
    return [char for char in word]

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        split_lines = []
        for word in input_lines:
            split_lines.append(split(word))

        split_lines.insert(0, ["." for i in range(len(split_lines[0]))])
        split_lines.append(["." for i in range(len(split_lines[0]))])

        for line in split_lines:
            line.insert(0, ".")
            line.append(".")

        return split_lines

def check_seat_num(input_lines, i, j):
    count = 0
    border = [-1,0,1]
    for x in border:
        for y in border:
            if not(x == 0 and y == 0):
                if input_lines[i+x][j+y] == "#":
                    count+=1
    return count

def check_seat_num_diag(input_lines, i, j):
    count = 0
    mul = 1
    border = [-1, 0, 1]

    for x in border:
        for y in border:
            # not looking at yourself
            #print("x: {} || y: {}".format(x, y))
            #print("i: {} || j: {}".format(i, j))
            #print(mul)

            if not(x == 0 and y == 0):
                while input_lines[i + mul*x][j + mul*y] == ".":
                    if (i + mul*x) == 0 or (i + mul*x) == (len(input_lines) - 1) or (j + mul*y) == 0 or (j + mul*y) == (len(input_lines[0]) - 1):
                        break
                    else:
                        mul+=1

                #print("row: {} || column: {}".format(i + mul*x, j + mul*y))



                if input_lines[i + mul*x][j + mul*y] == "L":
                    pass
                elif input_lines[i + mul*x][j + mul*y] == "#":
                    count+=1

                mul = 1

    return count

def iterate_seating(input_lines):
    new_iteration = copy.deepcopy(input_lines)

    for i in range(1, len(input_lines) - 1):
        for j in range(1, len(input_lines[i]) - 1):
            if input_lines[i][j] == "L" and check_seat_num(input_lines, i, j) == 0:
                new_iteration[i][j] = "#"
            elif input_lines[i][j] == "#" and check_seat_num(input_lines, i, j) >= 4:
                new_iteration[i][j] = "L"
            else:
                pass

    return new_iteration

def iterate_seating_diag(input_lines):
    new_iteration = copy.deepcopy(input_lines)

    for i in range(1, len(input_lines) - 1):
        for j in range(1, len(input_lines[i]) - 1):
            if input_lines[i][j] == "L" and check_seat_num_diag(input_lines, i, j) == 0:
                new_iteration[i][j] = "#"
            elif input_lines[i][j] == "#" and check_seat_num_diag(input_lines, i, j) >= 5:
                new_iteration[i][j] = "L"
            else:
                pass

    return new_iteration

def iterate_until_repition(input_lines):
    init_iteration = copy.deepcopy(input_lines)
    subseq_iteration = iterate_seating(init_iteration)

    while init_iteration != subseq_iteration:
        init_iteration = copy.deepcopy(subseq_iteration)
        subseq_iteration = iterate_seating(init_iteration)

    count = 0

    for x in init_iteration:
        for y in x:
            if y == "#":
                count+=1

    return count

def iterate_until_repition_diag(input_lines):
        init_iteration = copy.deepcopy(input_lines)
        subseq_iteration = iterate_seating_diag(init_iteration)

        while init_iteration != subseq_iteration:
            init_iteration = copy.deepcopy(subseq_iteration)
            subseq_iteration = iterate_seating_diag(init_iteration)

        count = 0

        for x in init_iteration:
            for y in x:
                if y == "#":
                    count+=1

        return count

if __name__ == "__main__":
    #iterate_seating(decode("test.txt"))
    #arr = decode("input1.txt")
    #print(len(arr))
    #print(arr[1])
    print(iterate_until_repition_diag(decode("input1.txt")))
