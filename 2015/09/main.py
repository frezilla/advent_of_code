#==============================================================================
# --- Day 9: All in a Single Night ---
#==============================================================================


class City:
    def __init__(self, name):
        self.name = name
        self.roads = set()


    def add_road(self, road):
        self.roads.add(road)


class Path:
    def __init__(self):
        self.roads = list()


    def add_road(self, road):
        self.roads.append(road)


    def distance(self):
        distance = 0
        for road in self.roads:
            distance += road.distance
        return distance


    def to_string(self):
        string = ''
        if len(self.roads) > 0:
            string += self.roads[0].start.name
            for road in self.roads:
                string += ' -> ' + road.to.name
        return string


class Road:
    def __init__(self, start : City, to : City, distance : int):
        self.start = start
        self.to = to
        self.distance = distance


    def to_string(self):
        return self.start.name + " - (" + str(self.distance) + ") -> " + self.to.name


def dfs(_city, visited : set, steps: list, paths: set):
    visited.add(_city)
    explore = False
    for road in _city.roads:
        if road.to not in visited:
            explore = True
            steps.append(road)
            dfs(road.to, visited, steps, paths)
            steps.pop()
            visited.remove(road.to)
    if not explore:
        path = Path()
        for road in steps:
            path.add_road(road)
        paths.add(path)

def run():
    print("--- Day 9: All in a Single Night ---")
    cities = dict()
    puzzle = open("puzzle.txt", 'r')
    for line in puzzle:
        datas = line.strip().split()
        city_name_1 = datas[0]
        city_name_2 = datas[2]
        distance = int(datas[4])
        city_1 = cities.setdefault(city_name_1, City(city_name_1))
        city_2 = cities.setdefault(city_name_2, City(city_name_2))
        city_1.add_road(Road(city_1, city_2, distance))
        city_2.add_road(Road(city_2, city_1, distance))
    puzzle.close()
    paths = set()
    for city in cities.values():
        dfs(city, set(), list(), paths)
    min_distance = 999999
    max_distance = 0
    for path in paths:
        if path.distance() < min_distance:
            min_distance = path.distance()
        if max_distance < path.distance():
            max_distance = path.distance()
    print(f"Distance minimale : {min_distance} et distance maximale : {max_distance}")


if __name__ == "__main__":
    run()


