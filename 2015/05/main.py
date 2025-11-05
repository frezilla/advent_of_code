#==============================================================================
# --- Day 5: Doesn't He Have Intern-Elves For This? ---
#==============================================================================


def init_letters():
    return {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
        "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }


def nice_string_part1():
    nice_strings = 0
    puzzle = open("puzzle.txt", "r")
    for line in puzzle:
        current_line = line.rstrip()
        if "ab" in current_line or "cd" in current_line or "pq" in current_line or "xy" in current_line:
            is_nice = False
        else:
            letters = init_letters()
            for letter in current_line:
                letters[letter] = letters[letter] + 1
            vowels = False
            if letters['a'] + letters['e'] + letters['i'] + letters['o'] + letters['u'] >= 3:
                vowels = True
            twice = False
            last_char = ""
            for letter in current_line:
                if last_char == letter:
                    twice = True
                    break
                else:
                    last_char = letter
            is_nice = vowels and twice
        if is_nice:
            nice_strings += 1
    puzzle.close()
    print(f"Part 1 : Number of nice strings: {nice_strings}")


def nice_string_part2():
    nice_strings = 0
    puzzle = open("puzzle.txt", "r")
    for line in puzzle:
        current_line = line.strip()
        length = len(current_line)
        is_nice = False
        if length > 0:
            index = 0
            repeat_letter = False
            while index < length:
                current_letter = current_line[index]
                if index + 2 < length and current_letter == current_line[index + 2]:
                    repeat_letter = True
                    break
                index += 1
            index = 0
            pair_letter = False
            while index < length:
                if index + 1 < length:
                    search_string = current_line[index:index + 2]
                    remaining_string = current_line[index + 2:]
                    if search_string in remaining_string:
                        pair_letter = True
                        break
                index += 1
            if repeat_letter and pair_letter:
                is_nice = True
        if is_nice:
            nice_strings += 1
    puzzle.close()
    print(f"Part 2 : Number of nice strings: {nice_strings}")


def run():
    print("--- Day 5: Doesn't He Have Intern-Elves For This? ---")
    nice_string_part1()
    nice_string_part2()


if __name__ == '__main__':
    run()