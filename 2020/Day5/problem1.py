def decoder(filepath):
    with open(filepath) as f:
        input_lines = [line.strip() for line in f]
        updated_list = []

        for line in input_lines:
            binary_translation = []
            for element in line:
                if element == "F" or element == "L":
                    binary_translation.append("0")
                else:
                    binary_translation.append("1")

            updated_list.append(binary_translation)

        input_lines = []

        for row in updated_list:
            input_lines.append("".join(row))

        return input_lines


def highestSeatID(list):
    max = 0
    for seat in list:
        #print("Row:  {} &  Col: {}".format(int(seat[:7], 2),int(seat[7:], 2)))
        value = (int(seat[:7], 2) * 8 + int(seat[7:], 2))
        if value > max:
            max = value
    return max

def orderSeats(list):
    flightSeats = []
    for seat in list:
        value = (int(seat[:7], 2) * 8 + int(seat[7:], 2))
        flightSeats.append(value)

    flightSeats = sorted(flightSeats)
    return(flightSeats)

def findSeat(list):
    for i in range(len(list) - 1):
        curSeat = list[i]
        nextSeat = list[i+1]
        if curSeat == (nextSeat - 2):
            return (curSeat + 1)

    return Print("Something went wrong")



print(findSeat(orderSeats(decoder("input1.txt"))))
