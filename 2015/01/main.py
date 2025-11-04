#==============================================================================
# --- Day 1: Not Quite Lisp ---
#==============================================================================


def run():
    print("--- Day 1: Not Quite Lisp ---")
    fhand = open("puzzle.txt", "r")
    instructions = ''
    for line in fhand:
        instructions += line.rstrip()
    floor = 0
    assign_position = True
    current_position = 1
    position = 0
    for x in instructions:
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1
        if floor == -1 and assign_position:
            assign_position = False
            position = current_position
        current_position += 1
    print(f"Etage final : {floor}")
    if position == 0:
        print("Santa n'est jamais allé à l'étage -1")
    else:
        print(f"Position du premier caractère qui a mené au sous_sol (étage -1) : {position}")


if __name__ == '__main__':
    run()