#==============================================================================
# --- Day 19: --- Medicine for Rudolph ---
#==============================================================================


def load_replacements():
    replacements = dict()
    puzzle = open("puzzle.txt", "r")
    for line in puzzle:
        current_line = line.rstrip()
        if len(current_line) == 0:
            break
        datas = current_line.split()
        current_values = replacements.setdefault(datas[0], list())
        current_values.append(datas[2])
        replacements.update({datas[0]: current_values})
    return replacements


def run():
    print("--- Day 19: --- Medicine for Rudolph ---")
    load_replacements()


if __name__ == '__main__':
    run()