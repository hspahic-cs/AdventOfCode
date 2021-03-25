'''
def count_words(filepath):
   with open(filepath) as f:
       input_lines = [line.strip() for line in f]
       return ((input_lines))
print(count_words("ch1_input.txt"))
'''

def calculate_fuel(filepath):
    with open(filepath) as f:
        input_lines = [line.strip() for line in f]
        sum = 0
        for x in input_lines:

            sum += (int(x) // 3) - 2

    return sum

print(calculate_fuel("ch1_input.txt"))
