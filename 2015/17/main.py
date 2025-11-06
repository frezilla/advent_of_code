#==============================================================================
# --- Day 17: No Such Thing as Too Much ---
#==============================================================================


def bit_value(value, index):
    return value >> (index - 1) & 1


def load_containers(filename):
    puzzle = open(filename, "r")
    result_list = list()
    for line in puzzle:
        current_line = line.strip()
        result_list.append(int(current_line))
    puzzle.close()
    return result_list


def select_containers(containers, str_combination):
    selected = list()
    for index in range(len(str_combination)):
        if str_combination[index] == '1':
            selected.append(containers[index])
    return selected


def to_string(value, size):
    str_value = str(bin(value))[2:]
    return str_value.zfill(size)


def run():
    print("--- Day 17: No Such Thing as Too Much ---")
    liters = 150
    containers = load_containers("puzzle.txt")
    max_value = ''.join('1' for i in range(len(containers)))
    max_value_size = len(max_value)
    max_value = int(max_value, 2)
    combinations = list()
    ways = dict()
    for combination in range(1, max_value + 1):
        str_combination = to_string(combination, max_value_size)
        str_combination = str_combination[::-1]
        selected = select_containers(containers, str_combination)
        current_value = 0
        str_selected = ''
        nb_selected = 0
        for current_container in selected:
            nb_selected += 1
            str_selected += str(current_container) + ' + '
            current_value += current_container
        if current_value == liters:
            str_select = str_selected[:-3]
            combinations.append(str_selected)
            result_list = ways.get(nb_selected, list())
            result_list.append(str_selected)
            ways.update({nb_selected:result_list})
    print(f"Nombre total de combinaisons : {len(combinations)}")
    min_key = 99999
    for k in ways.keys():
        if k < min_key:
            min_key = k
    print(f"Nombre total de manières : {len(ways.get(min_key))}")


if __name__ == "__main__":
    run()
