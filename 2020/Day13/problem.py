import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        input_lines[0] = int(input_lines[0])
        input_lines[1] = input_lines[1].split(",")
        working_busses = []

        for x in input_lines[1]:
            if x != "x":
                working_busses.append(int(x))
            else:
                pass


        input_lines[1] = working_busses
        return input_lines

def bus_diff(input_lines):
    min_time = 999999999999
    min_interval = 0

    for interval in input_lines[1]:
        print("{} multiple".format((input_lines[0]//interval + 1)))
        if ((input_lines[0]//interval + 1) * (interval) - input_lines[0]) < min_time:
            min_time = ((input_lines[0]//interval + 1) * (interval) - input_lines[0])
            min_interval = interval

    return min_interval * min_time

#This is chinese remainder thm. --> x = 1 remainder a | x = 2 remainder b | etc. || Order does not matter

def gcd(a, b):
    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b, rem)

# Runs pulverizer alg. and returns coeff a where exp in form | a mod b

def mod_inv(a, b):
    if gcd(a, b) != 1:
        return "Inputs are not relatively prime"

    if a == 1:
        return 1

    b0 = b
    x0, x1 = 0, 1

    while a > 1:
        q, rem = a // b, a % b
        a, b = b, rem
        x0, x1 = x1 - x0*q , x0
        #print("quot {} rem {} || x0 {} x1 {} || a {} b {}".format(q, rem, x0, x1, a ,b))

    while x1 < 0:
        x1 += b0

    return x1


# Initializes list of tuples accordingly (a, b) --> x = a mod b
def get_expressions(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        input_lines.pop(0)
        input_lines[0] = input_lines[0].split(',')
        input_lines = list(map(lambda x: int(x) if x != "x" else x, input_lines[0]))

        mod_expressions = []
        for i in range(len(input_lines)):
            if input_lines[i] != "x":
                mod_expressions.append((i, input_lines[i]))

        return mod_expressions

# Chinese Remainder Theorem for every element in list
def CRT(expressions):
    m = 1
    for exp in expressions:
        m *= exp[1]

    excl_list = []
    for i in range(len(expressions)):
        excl_list.append(m // expressions[i][1])

    excl_list_inverses = []
    for i in (range(len(excl_list))):
        excl_list_inverses.append(mod_inv(excl_list[i], expressions[i][1]))

    total = 0
    print(excl_list_inverses)
    for i in range(len(expressions)):
        print("{} exp || {} M || {} M inverse".format(expressions[i][0], excl_list[i], excl_list_inverses[i]))
        total += expressions[i][0] * excl_list[i] * excl_list_inverses[i]

    print(m - total % m)
    return total % m



if __name__ == "__main__":
    print(CRT(get_expressions("input.txt")))
    #print(gcd_rem_list(1, 5))
    print(mod_inv(247, 17))
