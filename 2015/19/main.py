#==============================================================================
# --- Day 19: --- Medicine for Rudolph ---
#==============================================================================


def create_molecule(value, key, replacement):
    indexes = search_all_indexes_of(value, key)
    molecules = list()
    for index in indexes:
        begin = value[:index]
        end = value[index:]
        end = end.replace(key, replacement, 1)
        molecules.append(begin + end)
    return molecules


def index_of(str, value):
    try:
        index = str.index(value)
    except ValueError:
        index = -1
    return index


def load_first_values():
    with open("puzzle.txt") as f:
        for line in f:
            pass
        last_line = line.rstrip()
    return last_line


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
    puzzle.close()
    return replacements


def run():
    print("--- Day 19: --- Medicine for Rudolph ---")
    replacements = load_replacements()
    initial_value = load_first_values()
    molecules = set()
    for key in replacements.keys():
        if key in initial_value:
            for replacement in replacements[key]:
                new_molecules = create_molecule(initial_value, key, replacement)
                for new_molecule in new_molecules:
                    molecules.add(new_molecule)
    print(f"Nombre de molécules uniques qui peuvent être créées : {len(molecules)}")
    replacement_reversed = dict()
    for key in replacements.keys():
        values = replacements.get(key)
        for value in values:
            replacement_reversed[value] = key
    keys = sorted(replacement_reversed.keys(), key=len, reverse=True)
    replacements_reversed_ordered = dict()
    for key in keys:
        replacements_reversed_ordered.update({key: replacement_reversed[key]})
    nb_steps = 0
    current_value = initial_value
    while current_value != "e":
        for key in replacements_reversed_ordered.keys():
            nb_indexes = len(search_all_distincts_indexes_of(current_value, key))
            if nb_indexes != 0:
                nb_steps += nb_indexes
                current_value = current_value.replace(key, replacements_reversed_ordered[key])
                break
    print(f"Nombre d'étapes pour générer la molécule cible : {nb_steps}")


def search_all_indexes_of(str, value, start_index = 0):
    result = list()
    index = index_of(str, value)
    if index != -1:
        result.append(index + start_index)
        if index + 1 < len(str):
            new_str = str[index + 1:]
            result = result + search_all_indexes_of(new_str, value, index + start_index + 1)
    return result


def search_all_distincts_indexes_of(str, value, start_index = 0):
    result = list()
    index = index_of(str, value)
    if index != -1:
        result.append(index + start_index)
        if index + len(value) < len(str):
            new_str = str[index + len(value):]
            result = result + search_all_distincts_indexes_of(new_str, value, index + len(value))
    return result


if __name__ == '__main__':
    run()