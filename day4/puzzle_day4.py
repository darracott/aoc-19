from collections import Counter

ub = 676461
lb = 178416

r = range(lb, ub)
# find all increasing monotonic sequences with 5 digits
digits = [0,1,2,3,4,5,6,7,8,9]

numbers = []
for d1 in digits:
    if (d1 < 1) or (d1 > 6):
        continue
    for d2 in list(range(d1, 10)):
        if (d1 == 1 and d2 < 7):
            continue
        if (d1 == 6 and d2 > 7):
            continue
        for d3 in list(range(d2, 10)):
            if d1 == 1 and d2 == 7 and d3 < 8:
                continue
            if d1 == 6 and d2 == 7 and d3 > 6:
                continue
            for d4 in list(range(d3, 10)):
                if d1 == 1 and d2 == 7 and d3 == 8 and d4 < 4:
                    continue
                if d1 == 6 and d2 == 7 and d3 == 6 and d4 > 4:
                    continue
                for d5 in list(range(d4, 10)):
                    if d1 == 1 and d2 == 7 and d3 == 8 and d4 == 4 and d5 < 1:
                        continue
                    if d1 == 6 and d2 == 7 and d3 == 6 and d4 == 4 and d5 > 6:
                        continue
                    for d6 in list(range(d5, 10)):
                        if d1 == 1 and d2 == 7 and d3 == 8 and d4 == 4 and d5 == 1 and d6 < 6:
                            continue
                        if d1 == 6 and d2 == 7 and d3 == 6 and d4 == 4 and d5 == 6 and d6 > 1:
                            continue
                        chosen_digits = [d1, d2, d3, d4, d5, d6]
                        #### start of part 2
                        if 2 not in Counter(chosen_digits).values():
                            continue
                        #### end of part 2 
                        number = int(
                            "".join(
                                [
                                    str(d1),
                                    str(d2),
                                    str(d3),
                                    str(d4),
                                    str(d5),
                                    str(d6)
                                ]
                            )
                        )
                        print(number)

                        numbers.append(number)
print(len(numbers))
