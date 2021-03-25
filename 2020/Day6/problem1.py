def decode(inputfile):
    with open(inputfile) as f:
        input_lines = [line.strip() for line in f]
        group = []
        updated_list = []
        for line in input_lines:
            if line != "":
                group.append(line)
            else:
                updated_list.append(group)
                group = []

        input_lines = []

        for row in updated_list:
            input_lines.append("".join(list(set("".join(row)))))

        return input_lines

def countQuestions(input):
    sum = 0
    for group in input:
        sum += len(group)

    return sum

def decodeRepeated(inputfile):
    with open(inputfile) as f:
        input_lines = [line.strip() for line in f]
        group = []
        updated_list = []
        for line in input_lines:
            if line != "":
                group.append(line)
            else:
                updated_list.append(group)
                group = []

        return(updated_list)

def split(word):
    return [char for char in word]

def commonQuestions(input):
    count = 0
    answers = []
    for group in input:
        print("This is the group: {}".format(group))
        for i in range(len(group)):
            if i == 0:
                answers = (split(group[i]))
                deep_answers = answers[:]
            else:
                for x in answers:
                    #print("Answers: {} & Deep Answers: {}".format(answers, deep_answers))
                    if not (x in split(group[i])):
                        #print("Group: {} Index: {} Element: {}".format(group, i, x))
                        deep_answers.remove(x)
                answers = deep_answers[:]

        print(answers)

        count+= len(answers)
        answers = []

    return count

print(commonQuestions(decodeRepeated("input1.txt")))
