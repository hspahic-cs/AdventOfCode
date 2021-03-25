import math

def decode(textfile):
    with open(textfile) as f:
        input_lines = [line.strip() for line in f]
        organized_list = []

        for line in input_lines:
            list = []
            list.append(line[0])
            list.append(line[1:])
            organized_list.append(list)

        return organized_list

# Note to self. Get into habit of naming function variables better
def chart_course(directions):
    x_pos = 0
    y_pos = 0
    direction = 0

    for command in directions:
        action = command[0]
        input = int(command[1])

        if action == "N":
            y_pos += input

        elif action == "S":
            y_pos -= input

        elif action == "E":
            x_pos += input

        elif action == "W":
            x_pos -= input

        # clockwise rotation
        elif action == "R":
            direction += input
            direction %= 360

        elif action == "L":
            direction -= input
            direction %= 360

        elif action == "F":
            if direction == 0:
                x_pos += input

            elif direction == 90:
                y_pos -= input

            elif direction == 180:
                x_pos -= input

            elif direction == 270:
                y_pos += input

            else:
                print("Something went wrong with Direction")

        else:
            print("Something went wrong with Action")

    return abs(x_pos) + abs(y_pos)

def waypoint_voyage(directions):
        x_pos = 0
        y_pos = 0

        wp_direction = 0
        wp_x_pos = 10
        wp_y_pos = 1

        for command in directions:
            action = command[0]
            input = int(command[1])

            if action == "N":
                wp_y_pos += input

            elif action == "S":
                wp_y_pos -= input

            elif action == "E":
                wp_x_pos += input

            elif action == "W":
                wp_x_pos -= input

            # clockwise rotation
            elif action == "R":
                input = (math.pi / 180) * input
                x = round(math.cos(input)*wp_x_pos + math.sin(input)*wp_y_pos)
                y = round(-math.sin(input)*wp_x_pos + math.cos(input)*wp_y_pos)
                wp_x_pos = x
                wp_y_pos = y

            elif action == "L":
                input = (math.pi / 180) * input
                x = round(math.cos(-input)*wp_x_pos + math.sin(-input)*wp_y_pos)
                y = round(-math.sin(-input)*wp_x_pos + math.cos(-input)*wp_y_pos)
                wp_x_pos = x
                wp_y_pos = y

            elif action == "F":
                x_pos += input*wp_x_pos
                y_pos += input*wp_y_pos

            else:
                print("Something went wrong with Action")

        return abs(x_pos) + abs(y_pos)

if __name__ == "__main__":
    print(waypoint_voyage(decode("input.txt")))
