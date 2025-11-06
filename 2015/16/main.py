#==============================================================================
# --- Day 16: Aunt Sue ---
#==============================================================================


class AuntSue:
    def __init__(self, _name):
        self.name = _name
        self.children = None
        self.children_indication = 'equal'
        self.cats = None
        self.cats_indication = 'greater'
        self.samoyeds = None
        self.samoyeds_indication = 'equal'
        self.pomeranians = None
        self.pomeranians_indication = 'fewer'
        self.akitas = None
        self.akitas_indication = 'equal'
        self.vizslas = None
        self.vizslas_indication = 'equal'
        self.goldfish = None
        self.goldfish_indication = 'fewer'
        self.trees = None
        self.trees_indication = 'greater'
        self.cars = None
        self.cars_indication = 'equal'
        self.perfumes = None
        self.perfumes_indication = 'equal'


    def check(self, _children, _cats, _samoyeds, _pomeranians, _akitas, _vizslas, _goldfish, _trees, _cars, _perfumes):
        return (self.check_field(self.children, _children)
                and self.check_field(self.cats, _cats)
                and self.check_field(self.samoyeds, _samoyeds)
                and self.check_field(self.pomeranians, _pomeranians)
                and self.check_field(self.akitas, _akitas)
                and self.check_field(self.vizslas, _vizslas)
                and self.check_field(self.goldfish, _goldfish)
                and self.check_field(self.trees, _trees)
                and self.check_field(self.cars, _cars)
                and self.check_field(self.perfumes, _perfumes))


    def check_field(self, field1, field2):
        if field1 is None:
            return True
        else:
            return field1 == field2


    def check_field_part2(self, field1, field2, indication):
        if field1 is None:
            return True
        else:
            if indication == 'fewer':
                return field1 < field2
            elif indication == 'greater':
                return field1 > field2
            else:
                return field1 == field2


    def check_part2(self, _children, _cats, _samoyeds, _pomeranians, _akitas, _vizslas, _goldfish, _trees, _cars, _perfumes):
        return (self.check_field_part2(self.children, _children, self.children_indication)
                and self.check_field_part2(self.cats, _cats, self.cats_indication)
                and self.check_field_part2(self.samoyeds, _samoyeds, self.samoyeds_indication)
                and self.check_field_part2(self.pomeranians, _pomeranians, self.pomeranians_indication)
                and self.check_field_part2(self.akitas, _akitas, self.akitas_indication)
                and self.check_field_part2(self.vizslas, _vizslas, self.vizslas_indication)
                and self.check_field_part2(self.goldfish, _goldfish, self.goldfish_indication)
                and self.check_field_part2(self.trees, _trees, self.trees_indication)
                and self.check_field_part2(self.cars, _cars, self.cars_indication)
                and self.check_field_part2(self.perfumes, _perfumes, self.perfumes_indication))


    def display(self):
        return ("""name: {}: children: {}, cats: {}, samoyeds: {}, pomeranians: {}, akitas: {}, vizslash: {}, goldfish: {}, trees: {}, cars: {}, perfumes: {}"""
        .format(
            self.name,
            str(self.children),
            str(self.cats),
            str(self.samoyeds),
            str(self.pomeranians),
            str(self.akitas),
            str(self.vizslas),
            str(self.goldfish),
            str(self.trees),
            str(self.cars),
            str(self.perfumes)))


def load_aunts(filename):
    puzzle = open(filename, "r")
    result_list = list()
    for line in puzzle:
        current_line = line.strip()
        datas = current_line.replace(":", "").replace(",", "").split()
        current_aunt = AuntSue(datas[0] + " " + datas[1])
        for index in range(2, len(datas), 2):
            if datas[index] == "children":
                current_aunt.children = int(datas[index + 1])
            elif datas[index] == "cats":
                current_aunt.cats = int(datas[index + 1])
            elif datas[index] == "samoyeds":
                current_aunt.samoyeds = int(datas[index + 1])
            elif datas[index] == "pomeranians":
                current_aunt.pomeranians = int(datas[index + 1])
            elif datas[index] == "akitas":
                current_aunt.akitas = int(datas[index + 1])
            elif datas[index] == "vizslas":
                current_aunt.vizslas = int(datas[index + 1])
            elif datas[index] == "goldfish":
                current_aunt.goldfish = int(datas[index + 1])
            elif datas[index] == "trees":
                current_aunt.trees = int(datas[index + 1])
            elif datas[index] == "cars":
                current_aunt.cars = int(datas[index + 1])
            elif datas[index] == "perfumes":
                current_aunt.perfumes = int(datas[index + 1])
        result_list.append(current_aunt)
    puzzle.close()
    return result_list

def run():
    print("--- Day 16: Aunt Sue ---")
    children = 3
    cats = 7
    samoyeds = 2
    pomeranians = 3
    akitas = 0
    vizslas = 0
    goldfish = 5
    trees = 3
    cars = 2
    perfumes = 1
    aunts = load_aunts("puzzle.txt")
    print("Partie 1")
    for aunt in aunts:
        if aunt.check(children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
            print(f"Tante Sue : {aunt.name}")
            print(f"{aunt.display()}")
    print("Partie 2")
    for aunt in aunts:
        if aunt.check_part2(children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
            print(f"Tante Sue : {aunt.name}")
            print(f"{aunt.display()}")


if __name__ == "__main__":
    run()
