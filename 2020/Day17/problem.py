import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        init_cube = []

        for line in input_lines:
            row = []
            for char in line:
                row.append(char)
            init_cube.append(row)

        init_cube = [init_cube]
        buffer_layer = [["." for x in range(len(init_cube[0]))] for y in range(len(init_cube[0]))]
        init_cube.append(copy.deepcopy(buffer_layer))
        init_cube.insert(0, copy.deepcopy(buffer_layer))

        return init_cube

# index = 3D tuple with cords (i, j, k) --> Checks if any particular cube is active or inactive
def check_cube(cube, index, active):
    buffer = [-1, 0, 1]
    count = 0

    for x in buffer:
        for y in buffer:
            for z in buffer:
                if not (x == 0 and y == 0 and z == 0):
                    #print(f"z {index[0] + z} || y {index[1] + y} || x {index[2] + x}")
                    if cube[index[0] + z][index[1] + y][index[2] + x] == "#":
                        count+=1

    if active:
        if not (count == 2 or count == 3):
            active = False
    else:
        if count == 3:
            active = True

    #print(count)
    return active

# adds buffer of inactive cubes to make sure index stays in bounds
def add_buffer(cube, INIT_BUFFER):
    corners = [1, len(cube) - 2]
    needs_buffer = False
    dim = len(cube[0]) + 2

    for x in range(len(cube)):
        for y in range(len(cube)):
            for z in range(len(cube)):
                if x in corners or y in corners or z in corners:
                    if cube[x][y][z] == "#":
                        needs_buffer = True
                        break

    if INIT_BUFFER == True:
        needs_buffer = True
        INIT_BUFFER = False

    if needs_buffer:
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

    return cube

def iterate_cube(cube):
    dupl_cube = copy.deepcopy(add_buffer(cube, False))
    for x in range(1, len(cube[0][0]) - 1):
        for y in range(1, len(cube[0]) - 1):
            for z in range(1, len(cube) - 1):
                if cube[z][y][x] == "#":
                    active = True
                else: active = False

                if check_cube(cube, (z,y,x), active):
                    dupl_cube[z][y][x] = "#"
                else: dupl_cube[z][y][x] = "."

    #display_cube(dupl_cube)
    return dupl_cube

def repeat_iteration(cube, n):
    while 0 < n:
        cube = iterate_cube(cube)
        n -= 1
        print("------------------------------------------------")

    return cube

def count_active(cube):
    count = 0
    for layer in cube:
        for row in layer:
            for char in row:
                if char == "#":
                    count += 1

    return count


def display_cube(cube):
    for layer in cube:
        print()
        for row in layer:
            print(row)

if __name__ == "__main__":
    cube = add_buffer(decode("test.txt"), True)
    display_cube(cube)
    #print(cube[2][5][4])
    print(count_active(repeat_iteration(cube, 6)))

    #cube = decode("test.txt")
    print(check_cube(cube, (2, 5, 4), False))
