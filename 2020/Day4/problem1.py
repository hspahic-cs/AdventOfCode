import string

# Function checks if input string
# has only hexdigits or not
def checkHexdigit(value):
    for letter in value:

        # If anything other than hexdigit
        # letter is present, then return
        # False, else return True
        if letter not in string.hexdigits[:16]:
            return False
    return True

def checkNum(value):
    for letter in value:

        # If anything other than hexdigit
        # letter is present, then return
        # False, else return True
        if letter not in string.hexdigits[:10]:
            return False
    return True



def decoder(filepath):
    with open(filepath) as f:
        input_lines = [line.strip() for line in f]
        org_list = []
        for x in input_lines:
            org_list.append(x.split(" "))

        return org_list

def simplify(org_list):
    temp_list = []
    new_list = []
    for inner_array in org_list:
        if inner_array != ['']:
            for y in inner_array:
                temp_list.append(y)
        else:
            new_list.append(temp_list)
            temp_list = []

    return new_list

def passportCounter(input):
    count = 0
    for x in input:
        if len(x) == 8:
            count+=1
        if len(x) == 7:
            bool = True
            for y in x:
                print(y[:3])
                if y[:3] == "cid":
                    bool = False
            if bool:
                count+=1
        #print("List {}: Count {}".format(x, count))

    print(count)

def validate(input):
    valid = False
    if len(input) == 8:
        valid = True
    if len(input) == 7:
        bool = True
        for y in input:
            if y[:3] == "cid":
                bool = False
        if bool:
            valid = True
    return valid


def detailedPassport(input):
    count = 0

    for person in input:
        print(sorted(person))
        if validate(person):
            bool = True
            for identifier in person:
                if identifier[:3] == "byr":
                    if not(int(identifier[4:])>= 1920 and  int(identifier[4:]) <= 2002):
                        bool = False
                    #['byr:1932', 'cid:226', 'ecl:grn', 'eyr:2025', 'hcl:#b6652a', 'hgt:156cm', 'iyr:2019', 'pid:715708549']

                elif identifier[:3] == "cid":
                    pass

                elif identifier[:3] == "ecl":
                    eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if not(identifier[4:] in eye_color):
                        bool = False

                elif identifier[:3] == "eyr":
                    #eyr
                    if not(len(identifier[4:]) == 4 and int(identifier[4:]) >= 2020 and int(identifier[4:]) <= 2030):
                        bool = False

                elif identifier[:3] == "hcl":

                    if not(len(identifier[5:]) == 6 and identifier[4] == "#" and checkHexdigit(identifier[5:])):
                        bool = False
                    

                elif identifier[:3] == "hgt":
                    if identifier[-2:] == "cm":
                        if not(int(identifier[4:-2]) >= 150 and int(identifier[4:-2]) <= 193):
                            bool = False
                    elif identifier[-2:] == "in":
                        if not(int(identifier[4:-2]) >= 59 and  int(identifier[4:-2]) <= 76):
                            bool = False
                    else:
                        bool = False



                elif identifier[:3] == "iyr":
                    if not(int(identifier[4:]) >= 2010 and int(identifier[4:]) <= 2020):
                        bool = False
                else:
                    if not(len(identifier[4:]) == 9 and checkNum(identifier[4:])):
                        bool = False

            if bool == True:
                count+=1

    print(count)


print(detailedPassport(simplify(decoder("input2.txt"))))
