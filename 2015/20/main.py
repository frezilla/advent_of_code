#==============================================================================
# --- Day 20: Infinite Elves and Infinite Houses ---
#==============================================================================


def get_dividers(value):
    result = set()
    a = 1
    b = value
    while a <= b and a not in result:
        b = int(value / a)
        if a * b == value:
            result.add(a)
            result.add(b)
        a = a + 1
    return result


class House:
    def __init__(self, number):
        self.number = number

    def get_presents1(self):
        dividers = get_dividers(self.number)
        value = 0
        for divider in dividers:
            value += divider * 10
        return value

    def get_presents2(self):
        dividers = sorted(get_dividers(self.number), reverse=True)
        value = 0
        for divider in dividers:
            if divider * 50 >= self.number:
                value += divider * 11
            else:
                break
        return value


def run():
    print("--- Day 20: Infinite Elves and Infinite Houses ---")
    puzzle_input = 29000000
    house_number = 1
    house = House(house_number)
    house_presents = house.get_presents1()
    while house_presents < puzzle_input:
        house_number += 1
        house = House(house_number)
        house_presents = house.get_presents1()
    print(f"Première partie : La maison numéro {house_number} est la première maison dont la valeur dépasse la valeur {puzzle_input}")
    house = House(house_number)
    house_presents = house.get_presents2()
    while house_presents < puzzle_input:
        house_number += 1
        house = House(house_number)
        house_presents = house.get_presents2()
    print(f"Deuxième partie : La maison numéro {house_number} est la première maison dont la valeur dépasse la valeur {puzzle_input}")


if __name__ == "__main__":
    run()