import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]

    return input_lines

def check_sign(cmd):
    if cmd[4] == "+":
        return True
    else: return False

def find_loop(cmds):
    acc = 0
    repeated_lines = []
    index = 0
    while not index in repeated_lines:
        repeated_lines.append(index)
        arg = int(cmds[index][5:])
        if cmds[index][0:3] == "acc":
            if check_sign(cmds[index]):
                acc += arg
            else:
                acc -= arg
            index += 1

        elif cmds[index][0:3] == "jmp":
            if check_sign(cmds[index]):
                index += arg
            else:
                index -= arg

        else:
            index += 1

    return acc

def count_acc(cmds):
    acc = 0
    index = 0
    while index < len(cmds):
        arg = int(cmds[index][5:])
        if cmds[index][0:3] == "acc":
            if check_sign(cmds[index]):
                acc += arg
            else:
                acc -= arg
            index += 1

        elif cmds[index][0:3] == "jmp":
            if check_sign(cmds[index]):
                index += arg
            else:
                index -= arg

        else:
            index += 1

    return acc
# ============================================================================ #

def check_cmds(cmds):
    repeated_lines = []
    index = 0
    while not index in repeated_lines:
        repeated_lines.append(index)
        arg = int(cmds[index][5:])

        if cmds[index][0:3] == "jmp":
            if check_sign(cmds[index]):
                index += arg
            else:
                index -= arg
        else:
            index += 1

        if (index) == len(cmds):
            return True

    return False

def fix_program(cmds):
        potential_bugs = []
        repeated_lines = []
        pot_bug_index = 0
        index = 0
        bug_found = False

        for x in range(len(cmds)):
            if (cmds[x][0:3] == "jmp" or cmds[x][0:3] == "nop"):
                potential_bugs.append(x)

        while not bug_found:
            alt_cmds = copy.deepcopy(cmds)
            print(potential_bugs)
            pot_bug_index = potential_bugs[0]
            if alt_cmds[pot_bug_index][0:3] == "jmp":
                alt_cmds[pot_bug_index] = alt_cmds[pot_bug_index].replace("jmp", "nop")
            else:
                alt_cmds[pot_bug_index] = alt_cmds[pot_bug_index].replace("nop", "jmp")

            bug_found = check_cmds(alt_cmds)
            potential_bugs.pop(0)

        return count_acc(alt_cmds)


if __name__ == "__main__":
    print(fix_program(decode("test.txt")))
