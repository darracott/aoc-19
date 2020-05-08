from common.functions import load_input


def list_orbiters(orbitees, orbiter_relations):
    orbiters = []
    for orbitee in orbitees:
        new_orbiters = orbiter_relations.get(orbitee)
        if new_orbiters:
            orbiters += new_orbiters
    return orbiters


def rec_list_orbiters(orbiter_relations):
    orbits = [["COM"]]
    while True:
        orbiters = list_orbiters(orbits[-1], orbiter_relations)
        if not orbiters:
            break
        orbits.append(orbiters)
    return orbits


def main():
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

    orbits = rec_list_orbiters(orbiter_relations)

    count = 0
    for weight, orbit in enumerate(orbits):
        count += weight * len(orbit)

        if "YOU" in orbit:
            you_depth = weight
            # print(f"Orbit depth of 'YOU': {weight}")
        if "SAN" in orbit:
            san_depth = weight
            # print(f"Orbit depth of 'SAN': {weight}")

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
    position1 = get_orbitee[start]
    position2 = get_orbitee[target]

    while position1 != position2:
        position1 = get_orbitee[position1]
        position2 = get_orbitee[position2]
        distance += 2

    return count, distance


if __name__ == "__main__":
    count, distance = main()
    print(f"Distance is: {distance}")
    print(f"Count is: {count}")
