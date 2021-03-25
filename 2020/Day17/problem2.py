import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        init_tes = []

        for line in input_lines:
            row = []
            for char in line:
                row.append(char)
            init_tes.append(row)



        init_tes = [init_tes]
        dim = len(init_tes[0])
        buffer_layer = [["." for x in range(dim)] for y in range(dim)]
        buffer_tes = [[["." for x in range(dim)] for y in range(dim)] for z in range(dim)]
        init_tes.append(copy.deepcopy(buffer_layer))
        init_tes.insert(0, copy.deepcopy(buffer_layer))
        init_tes = [init_tes]
        init_tes.append(copy.deepcopy(buffer_tes))
        init_tes.insert(0, copy.deepcopy(buffer_tes))

        return init_tes

# index = 3D tuple with cords (i, j, k) --> Checks if any particular tes is active or inactive
def check_tes(tes, index, active):
    buffer = [-1, 0, 1]
    count = 0

    for x in buffer:
        for y in buffer:
            for z in buffer:
                for w in buffer:
                    if not (x == 0 and y == 0 and z == 0 and w == 0):
                        #print(f"w {index[0] + w}|| z {index[1] + z} || y {index[2] + y} || x {index[3] + x}")
                        if tes[index[0] + w][index[1] + z][index[2] + y][index[3] + x] == "#":
                            count+=1

    if active:
        if not (count == 2 or count == 3):
            active = False
    else:
        if count == 3:
            active = True

    #print(count)
    return active

# adds buffer of inactive tess to make sure index stays in bounds
def add_buffer(tes, INIT_BUFFER):
    corners = [1, len(tes) - 2]
    needs_buffer = False
    dim = len(tes[0][0]) + 2

    for x in range(len(tes)):
        for y in range(len(tes)):
            for z in range(len(tes)):
                for w in range(len(tes)):
                    if x in corners or y in corners or z in corners or w in corners:
                        if tes[w][z][y][x] == "#":
                            needs_buffer = True
                            break

    if INIT_BUFFER == True:
        needs_buffer = True
        INIT_BUFFER = False

    if needs_buffer:
        for cube in tes:
            for layer in cube:
                for row in layer:
                    row.append(".")
                    row.insert(0, ".")

                buffer_row = ["." for x in range(dim)]
                layer.append(copy.deepcopy(buffer_row))
                layer.insert(0, copy.deepcopy(buffer_row))


            buffer_layer = [["." for x in range(dim)] for y in range(dim)]
            cube.append(copy.deepcopy(buffer_layer))
            cube.insert(0, copy.deepcopy(buffer_layer))

        buffer_tes = [[["." for x in range(dim)] for y in range(dim)] for z in range(dim - 1)]
        tes.append(copy.deepcopy(buffer_tes))
        tes.insert(0, copy.deepcopy(buffer_tes))


        center_cube = int(len(tes) / 2)
        #print(f"Center index {center_cube} || Num Cubes {len(tes)}")
        while(len(tes[center_cube]) < dim):
            buffer_layer = [["." for x in range(dim)] for y in range(dim)]
            tes[center_cube].append(copy.deepcopy(buffer_layer))
            tes[center_cube].insert(0, copy.deepcopy(buffer_layer))

    return tes

def iterate_tes(tes):
    dupl_tes = copy.deepcopy(add_buffer(tes, False))
    #display_tes(dupl_tes[2])
    #print(len(dupl_tes[5]))
    for x in range(1, len(tes[0][0][0]) - 1):
        for y in range(1, len(tes[0][0]) - 1):
            for z in range(1, len(tes[0]) - 1):
                for w in range(1, len(tes) - 1):
                    if tes[w][z][y][x] == "#":
                        active = True
                    else: active = False

                    if check_tes(tes, (w,z,y,x), active):
                        dupl_tes[w][z][y][x] = "#"
                    else: dupl_tes[w][z][y][x] = "."


    #display_tes(dupl_tes)
    return dupl_tes

def repeat_iteration(tes, n):
    while 0 < n:
        tes = iterate_tes(tes)
        display_tes(tes)
        n -= 1
        print("------------------------------------------------")

    return tes

def count_active(tes):
    count = 0
    for cube in tes:
        for layer in cube:
            for row in layer:
                for char in row:
                    if char == "#":
                        count += 1

    return count


def display_tes(tes):
    for cube in tes:
        print()
        for layer in cube:
            print()
            for row in layer:
                print(row)

if __name__ == "__main__":
    #tes = decode("test.txt")
    #print(tes)
    #display_tes(tes)
    tes = add_buffer(decode("input.txt"), True)
    #display_tes(tes)
    #print(tes[2][5][4])
    print(count_active(repeat_iteration(tes, 6)))


    #tes = decode("test.txt")
    #print(check_tes(tes, (2, 5, 4), False))
