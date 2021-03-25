import copy

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        intervals, my_ticket, other_tickets, labels = [], [], [], []
        space = 0

        for line in input_lines:
            if not line:
                space+=1
            elif space == 0:
                line = line.split(": ")
                labels.append(line.pop(0))
                line = line[0].split(" ")
                line.pop(1)
                val = []
                for x in line:
                    y = x.split("-")
                    val.append(y)

                intervals.append(val)

            elif space == 1:
                if not line == "your ticket:":
                    my_ticket.append(line.split(","))

            else:
                if not line == "nearby tickets:":
                    other_tickets.append(line.split(","))

        return intervals, my_ticket, other_tickets, labels

# Intervals == list until first space
def check_value(intervals, value):
    bool = False
    for x in intervals:
        for range in x:
            if (int(range[0]) <= value <= int(range[1])):
                bool = True
    return bool

# List = all values after first space
def vertify_ticket(intervals, my_ticket, other_tickets):
    tickets = copy.deepcopy(other_tickets)
#    for ticket in other_tickets:
#        tickets.append(ticket)

    remove = []
    debug = []
    sum = 0
    i, j = 0, 0
    for ticket in tickets:
        for element in ticket:
            if not check_value(intervals, int(element)):
                remove.append(ticket)
                #debug.append(element)
                sum += int(element)

    for element in remove:
        tickets.remove(element)

    #print(sum)
    return tickets


# Returns a list of how many intervals each column of ticket satisfies
def determine_row_count(intervals, tickets, labels):
    indices = []
    dupl = copy.deepcopy(intervals)
    count = 0
    dupl_labels = [0 for x in range(20)]
    key = [[] for i in range(20)]

    for i in range(len(intervals)):
        for k in range(len(intervals)):
            for j in range(len(tickets)):
                value = int(tickets[j][k])
                if not ((int(dupl[i][0][0]) <= value <= int(dupl[i][0][1]) or int(dupl[i][1][0]) <= value <= int(dupl[i][1][1]))):
                    #print(f" label {(labels[i])} : {value} : {intervals[i+1]}")
                    break

                if j == len(tickets) - 1:
                    dupl_labels[i] += 1
                    key[k].append(labels[i])

    print(key[12])
    return dupl_labels, key

def determine_row_order(intervals, tickets, labels, frequencies, key, my_ticket):
    dupl = copy.deepcopy(key)
    for i in range(len(key)):
        if len(key[i]) == 1:
            init_catg = key[i][0]
        if len(key[i]) == 20:
            max_index = i

    while 1 < len(dupl[max_index]):
        init_catg_copy = init_catg
        for i in range(len(dupl)):
            if len(dupl[i]) != 1:
                dupl[i].remove(init_catg_copy)
                if len(dupl[i]) == 1:
                    init_catg = dupl[i][0]

    product = 1
    for i in range(len(dupl)):
        if len(dupl[i][0]) >= 8 and dupl[i][0][:9] == "departure":
            product *= int(my_ticket[0][i])

    print(product)

    return dupl

def debugger(tickets, one, two, three, four):
    for i in range(len(tickets)):
        for j in range(len(tickets[i])):
            value = int(tickets[i][j])
            if value < one or two < value < three or four < value:
                print(f"val {value} : i {i} : j {j}")


if __name__ == "__main__":
    data = decode("input.txt")
    intervals, my_ticket, other_tickets, labels = data[0], data[1], data[2], data[3]
    tickets = vertify_ticket(intervals, my_ticket, other_tickets)  # Vertify Tickets is working correctly
    frequencies, key = determine_row_count(intervals, tickets, labels)
    print(frequencies)
    print(determine_row_order(intervals, tickets, labels, frequencies, key, my_ticket))
    debugger(tickets, 50, 561, 567, 964)
