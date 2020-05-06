from day1.puzzle_day1 import load_input


def list_orbiters(orbitees):
    orbiters = []
    for orbitee in orbitees:
        new_orbiters = orbiter_relations.get(orbitee)
        if new_orbiters:
            orbiters += new_orbiters
    return orbiters


def rec_list_orbiters():
    orbits = [["COM"]]
    while True:
        orbiters = list_orbiters(orbits[-1])
        if not orbiters:
            break
        orbits.append(orbiters)
    return orbits


if __name__ == "__main__":
    map_data = load_input(6)
    orbiter_relations = {}  # Dict[str, List[str]]
    get_orbitee = {}
    for orbit in map_data:
        orbit = orbit.strip()
        orbitee, orbiter = orbit.split(")")
        get_orbitee[orbiter] = orbitee
        if orbiter_relations.get(orbitee):
            orbiter_relations[orbitee].append(orbiter)
        else:
            orbiter_relations[orbitee] = [orbiter]

    orbits = rec_list_orbiters()
    
    count = 0
    for weight, orbit in enumerate(orbits):
        count += weight * len(orbit)

        if "YOU" in orbit:
            you_depth = weight
            print(f"Orbit depth of 'YOU': {weight}")
        if "SAN" in orbit:
            san_depth = weight
            print(f"Orbit depth of 'SAN': {weight}")

    print(orbits[219])
    
    if san_depth >= you_depth:
        start = "SAN"
        target = "YOU"
        depth = san_depth
        end_depth = you_depth
    else:
        start = "YOU"
        target = "SAN"
        depth = you_depth
        end_depth = san_depth

    while depth != end_depth:
        new_start = get_orbitee[start]
        start = new_start
        depth -= 1
    
    distance = abs(you_depth - san_depth)
    print(distance)
    position1 = get_orbitee[start]
    position2 = get_orbitee[target]
    print(position1)
    print(position2)

    while position1 != position2:
        position1 = get_orbitee[position1]
        position2 = get_orbitee[position2]
        distance += 2
    print(position1)
    print(position2)
    print(distance)


# class DAG(object):
#     """
#     """
#     def __init__(self, data):
#         self.data = data
#         # TODO read effective python on data structures for DAG 
#         for line in data:
#             print(line)