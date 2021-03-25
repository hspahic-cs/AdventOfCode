import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip().split() for line in f]
        dupl = []
        dupl_piece = []
        for line in input_lines:
            for chunk in line:
                if chunk[0] == "(":
                    i = 0
                    while chunk[i] == "(":
                        dupl_piece.append("(")
                        i+=1
                    dupl_piece.append(chunk[-1])

                elif chunk[-1] == ")":
                    dupl_piece.append(chunk[0])
                    i = 1
                    while chunk[-i] == ")":
                        dupl_piece.append(")")
                        i+=1

                else:
                    dupl_piece.append(chunk)

            dupl.append(dupl_piece)
            dupl_piece = []

        return dupl

def simp_add(expression):
    if "+" in expression:
        index = expression.index("+")
        current_val = int(expression[index - 1]) + int(expression[index + 1])
        expression[index + 1] = current_val
        expression.pop(index - 1)
        expression.pop(index - 1)
        return simp_add(expression)
    else:
        return expression

def simp_prt(expression):
    #print(f"operator {operator} || current_val {current_val}")
    #print(expression)
    expression = simp_add(expression)
    current_val = int(expression[0])
    operator = ""
    expression = expression[1:]

    for term in expression:
        if term == "*":
            operator = term
        elif term == ")":
            return current_val
        else:
            current_val *= int(term)

    return current_val

def simp_exp(expression):
    left_index = 0
    right_index = 0
    current_val = 0
    operator = ""
    i = 0

    if ")" in expression:
        while i < len(expression):
            exp = expression[i]
            if exp == "(":
                left_index = i
            elif exp == ")":
                right_index = i
                expression[left_index] = (simp_prt(expression[left_index + 1:right_index]))
                remove = right_index - left_index
                while remove > 0:
                    expression.pop(left_index + 1)
                    remove -= 1
                return simp_exp(expression)

            elif current_val == 0:
                current_val = int(exp)
            elif exp == "+" or exp == "*":
                operator = exp
            else:
                if operator == "+":
                    current_val += int(exp)
                else:
                    current_val *= int(exp)

            i+=1

    elif "+" in expression:
        return simp_exp(simp_add(expression))

    else:
        for term in expression:
            if current_val == 0:
                current_val = int(term)
            elif term == "*":
                operator = term
            else:
                current_val *= int(term)

    return current_val

def iterate(list):
    sum = 0
    for expression in list:
        sum += (simp_exp(expression))

    return sum

if __name__ == "__main__":
    list = (decode("input.txt"))
    print(iterate(list))
