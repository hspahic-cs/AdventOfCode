import copy

def split(word):
    return [char for char in word]

# Creates list with format [[Rule1] [Rule2] ... etc] --> RuleX = ["adj", "color", "#", "adj", "color" --> etc]

def decode(inputfile):
    with open(inputfile) as f:
        input_lines = [line.strip() for line in f]
        org_list = []
        for x in input_lines:
            org_list.append(x.split(" "))

        org_list_dc = copy.deepcopy(org_list)

        for i in range(len(org_list)):
            for word in org_list[i]:
                if word == "bags" or word == "contain" or word == "bag," or word == "bags," or word == "bag." or word == "bags." or word == "no" or word == "other":
                    org_list_dc[i].remove(word)

        return org_list_dc

# Make a class -->
class Bag:
    def __init__(self, contents):
        self.name = contents[0] + " " + contents[1]
        self.insideBags = {}
        for i in range(2, len(contents), 3):
            self.insideBags.update({contents[i+1] + " " +  contents[i+2] : int(contents[i])})

    def __str__ (self):
        return str("Name: {} || {}".format(self.name, self.insideBags))

class BagList:
    def __init__(self, contents):
        self.bagList = []
        for bag in contents:
            self.bagList.append(Bag(bag))

    def findPossibleBags(self, bagColors):
        colorCount = 0
        print(bagColors)
        colorList = []
        for bag in self.bagList:
            for color in bagColors:
                if color in bag.insideBags:
                    colorCount += 1
                    colorList.append(bag.name)
                    break

        for color in colorList:
            for bag in self.bagList:
                if color == bag.name:
                    self.bagList.remove(bag)

        if colorCount == 0:
            return 0

        return colorCount + self.findPossibleBags(colorList)

    def findBag(self, bagName):
        for bag in self.bagList:
            if bag.name == bagName:
                return bag

    def numberOfBags(self, bag):
        sum = 0
        for key in bag.insideBags:
            sum += bag.insideBags[key] + bag.insideBags[key] * self.numberOfBags(self.findBag(key))


        return sum



if __name__ == "__main__":
    #print(decode("test.txt"))
    contents = decode("input2.txt")
    allCombos = BagList(contents)
    print(allCombos.numberOfBags(allCombos.findBag("shiny gold")))
