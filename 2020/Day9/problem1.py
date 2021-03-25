import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]

    return input_lines


def check_subq(pot_sum_arr, target):
    sum = 0
    for first in pot_sum_arr:
        for second in pot_sum_arr:
            if first != second:
                sum = int(first) + int(second)

            if sum == int(target):
                return True

    return False

def find_error(input_lines, len_preamble):
    current_list = []
    dupl = copy.deepcopy(input_lines)
    for x in range(len_preamble):
        current_list.append(dupl.pop(0))

    target_found = False
    while not target_found:
        target_found = not(check_subq(current_list, dupl[0]))
        current_list.pop(0)
        current_list.append(dupl.pop(0))


    return current_list[len(current_list) - 1]

def xmas_weakness(input_lines, error):
    subq_sum = 0
    dupl = copy.deepcopy(input_lines)
    pot_num = []
    while subq_sum != error:
        for x in dupl:
            print(subq_sum)
            if subq_sum > error:
                dupl.pop(0)
                pot_num = []
                subq_sum = 0
                break
            elif subq_sum == error:
                break
            else:
                pot_num.append(x)
                subq_sum += int(x)

    pot_num = list(map(int, pot_num))
    return max(pot_num) + min(pot_num)


if __name__ == "__main__":
    input_lines = decode("input1.txt")
    print(xmas_weakness(input_lines, int(find_error(input_lines, 25))))
