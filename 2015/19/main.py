#==============================================================================
# --- Day 19: --- Medicine for Rudolph ---
#==============================================================================


def load_replacements():
    puzzle = open("puzzle.txt", "r")
    for line in puzzle:
        current_line = line.rstrip()
        if len(current_line) == 0:
            break


def run():
    print("--- Day 19: --- Medicine for Rudolph ---")
    load_replacements()


if __name__ == '__main__':
    run()