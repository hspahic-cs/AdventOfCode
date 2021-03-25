import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        rules, inputs = [], []
        toggle = False
        for line in input_lines:
            if line == "":
                toggle = True
                pass
            elif not toggle:
                rules.append(line)
            else:
                inputs.append(line)

        rules = [line.split() for line in rules]
        dupl = {}

        for rule in rules:
            dupl.update({rule[0][0:-1]:rule[1:]})

        rules = dupl

        return rules, inputs

def encode_rules(rules, key):
    if rules[key][0] == 'a' or rules[key][0] == 'b':
        return rules[key][0]
    elif "|" in rules[key]:
        if len(rules[key]) == 5:
            print(f"Row with | {rules[key][0]} : {rules[key][1]} : {rules[key][3]} : {rules[key][4]} ")
            return [[encode_rules(rules, rules[key][0])] + [encode_rules(rules, rules[key][1])]] + [[encode_rules(rules, rules[key][3])] + [encode_rules(rules, rules[key][4])]]
        elif len(rules[key]) == 3:
            print(f"Row with | {rules[key][0]} : {rules[key][2]} ")
            return [encode_rules(rules, rules[key][0])] + [encode_rules(rules, rules[key][2])]
    else:
        print(rules[key])
        concat = []
        for term in rules[key]:
            print(term)
            concat.append(encode_rules(rules, term))

        return concat

def gen_valid_key(encode_rules):
    if 


if __name__ == "__main__":
    rules, inputs = decode("test.txt")
    #print(rules)
    #print(inputs)
    print(encode_rules(rules, "0"))
    #rules, inputs = decode("UT.txt")
    #print(rules, inputs)
