def calculate_fuel(filepath):
    with open(filepath) as f:
        input_lines = [line.strip() for line in f]
        sum = 0
        for x in input_lines:
            sum+= recursive_fuel((int(x) // 3) - 2)

    return sum

def recursive_fuel(init_fuel):
    new_fuel = (init_fuel // 3) - 2
    if new_fuel <= 0:
        return init_fuel
    else:
        return init_fuel + recursive_fuel(new_fuel)

print(calculate_fuel("ch2_input.txt"))
