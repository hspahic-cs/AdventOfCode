import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [int(line.strip()) for line in f]

    return input_lines

def chain_adapters(input_lines):
    cur_adapter = 0
    count_dif = [0,0,0]
    # count_dif[i] --> count of dif of i + 1
    dupl = (sorted(copy.deepcopy(input_lines)))
    dupl.append(dupl[-1]+3)
    print(dupl)
    for adapter in dupl:
        print("adapter {} | cur_adapter {}".format(adapter, cur_adapter))
        if cur_adapter + 3 < adapter:
            break
        else:
            dif = adapter - cur_adapter
            print(dif)
            count_dif[dif - 1] += 1
            cur_adapter = adapter


    print(len(dupl))
    return count_dif[0] * count_dif[2]


def count_combos(chunk):
    combos = 1
    num_deleted = 1

    while (num_deleted < 3):

        if num_deleted == 1:
            for i in range(len(chunk) - 2):
                dupl = copy.deepcopy(chunk)
                dupl[i+1] += dupl[i]
                if dupl[i+1] > 3:
                    pass
                else:
                    combos += 1

            num_deleted+=1

        elif num_deleted == 2:
            for i in range(len(chunk) - 2):
                dupl = copy.deepcopy(chunk)
                val = dupl.pop(i)
                for j in range(len(dupl) - 2):
                    if j != i:
                        dupl2 = copy.deepcopy(dupl)
                        val += dupl2.pop(j)
                        dupl2[j] += val
                        if max(dupl2) > 3:
                            pass
                        else:
                            combos += 1

            num_deleted += 1

    return combos

def valid_combos(input_lines):
    dupl = (sorted(copy.deepcopy(input_lines)))
    dupl.insert(0,0)
    dif_list = [dupl[i+1] - dupl[i] for i in range(len(dupl) - 1)]
    dif_list.append(3)
    print(dif_list)
    print(len(dif_list))
    chunk = []
    current_index = 0
    num_combos = 1
    for i in range(len(dif_list)):
        if dif_list[i] == 3:
            chunk = copy.deepcopy(dif_list[current_index:i+1])
            print("{} {} current index & {} num_combos".format(chunk,current_index, count_combos(chunk)))
            num_combos *= count_combos(chunk)
            current_index = i+1

    return num_combos


if __name__ == "__main__":
    #print(chain_adapters(decode("test.txt")))
    print(valid_combos(decode("input1.txt")))
