import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip().split(',') for line in f]
        upd = []

        for element in input_lines:
            upd.append(list(map(int, element)))

        return upd

def memory_game(gap, init_list):
    init_list = copy.deepcopy(init_list[0])
    distance = {}

    print(init_list)
    for i in range(len(init_list)):
        distance.update({init_list[i]: i})

    for k in range(gap):
        cur_pos = (len(init_list) - 1)
        number = init_list[-1]
        #print(f"cur_pos {cur_pos} || Number Distance {distance} || Num {number} ")


        if number in distance:
            init_list.append(cur_pos - distance[number])

        else:
            init_list.append(0)

        distance.update({number:cur_pos})

    #print(init_list)
    return init_list[30000000 - 1]

if __name__ == "__main__":
    print(memory_game(30000000,decode("test.txt")))
