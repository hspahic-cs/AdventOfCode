#"{0:b}".format(111111002010)
import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        return input_lines


# str_num is the string of the number provided in input

class BinaryNum():
    def __init__(self, str_num, base10, *args):
        self.digits = []
        count = 0

        if base10 == True:
            str_num = "{0:b}".format(int(str_num))

        for char in str_num:
            if char != "X": self.digits.append(int(char))
            else:
                self.digits.append(char)
                count+=1

        while len(self.digits) < 36:
            self.digits.insert(0, 0)

        if args:
            index = "{0:b}".format(int(args[0]))
            self.index = []
            for num in index:
                self.index.append(num)

            while len(self.index) < 36:
                self.index.insert(0,0)
        else:
            self.count = count
        #print(self.digits)

    def apply_mask(self, mask):
        for i in range(len(self.digits)):
            if mask.digits[i] != "X":
                self.digits[i] = mask.digits[i]

    def decimal_sum(self):
        sum = 0
        for i in range(len(self.digits)):
            sum += 2**(35 - i) * self.digits[i]

        return sum


class BinaryNumList():
    def __init__(self):
        self.binaryDict = {}

    def append(self, BinaryNum, index):
        self.binaryDict.update({index:BinaryNum.digits})

    def find_sum(self):
        sum = 0
        for key in self.binaryDict:
            sum += (decimal_sum(self.binaryDict[key]))

        return sum

# Schrodinger's Binary Number
class SdgBinNum(BinaryNum):
    def __init__(self, str_num, base10, *args):
        super().__init__(str_num, base10, *args)


    def apply_mask(self, mask):
        for i in range(len(self.index)):
            if mask.digits[i] == 1 or mask.digits[i] == "X":
                self.index[i] = mask.digits[i]

    def decimal_conv(self):
        sum = 0
        for i in range(len(self.index)):
            for j in range(len(self.index[i])):
                sum += 2**(35 - j) * int(self.index[i][j])

            self.index[i] = sum
            sum = 0

    '''def decimal_sum(self):
        sum = 0
        for i in range(len(self.digits)):
            sum += 2**(35 - i) * self.digits[i]

        return sum'''

def create_list(input_lines):
    nums = BinaryNumList()

    for line in input_lines:
        if line[:3] != "mem":
            cur_mask = BinaryNum(line[7:], False)
        else:
            print(line)
            values = line.split("]")
            bin_num = BinaryNum(values[1][3:], True, int(values[0][4:]))
            bin_num.apply_mask(cur_mask)
            nums.append(bin_num)
            print("{} values \n {} BinaryNum \n {} mask \n".format(values, bin_num.digits, cur_mask.digits))

    return nums

def create_sdg_list(input_lines):
    nums = BinaryNumList()

    for line in input_lines:
        if line[:3] != "mem":
            cur_mask = BinaryNum(line[7:], False)
        else:
            values = line.split("]")
            bin_num = SdgBinNum(values[1][3:], True, values[0][4:])
            print(f"number {values[1][3:]} || index {values[0][4:]}")
            bin_num.apply_mask(cur_mask)
            bin_num.index = chunkIt(create_branches(bin_num.index, -1), 2**cur_mask.count)
            if values[0][4:] == "3341":
                for line in bin_num.index:
                    print(line)
            bin_num.decimal_conv()

            #print(bin_num.digits)
            for num in bin_num.index:
                #print(bin_num.digits)
                nums.append(bin_num, num)


    return nums

def create_branches(list, i):
    dupl1 = copy.deepcopy(list)
    dupl2 = copy.deepcopy(list)
    if i == 35:
        return list

    for index in range(i+1,len(list)):


        if list[index] == "X":
            dupl1[index] = 0
            dupl2[index] = 1
            return create_branches(dupl1, index) + create_branches(dupl2, index)
            #print("dupl1: {} \ndupl2: {}".format(dupl1, dupl2))
        elif index == 35:
            return list


def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def decimal_sum(list):
    sum = 0
    for i in range(len(list)):
        sum += 2**(35 - i) * list[i]

    return sum

if __name__ == "__main__":
    '''
    num = SdgBinNum("100", True, 42)
    mask = BinaryNum("000000000000000000000000000000X1001X", False)
    num.apply_mask(mask)
    print(num.index)
    num.index = chunkIt(create_branches(num.index, 0), 2**mask.count)
    #print(num.decimal_sum)
    #for line in num.index:
    #    print(line)
    #print(num.decimal_sum())
    '''
    commands = (decode("input.txt"))
    print(create_sdg_list(commands).find_sum())
