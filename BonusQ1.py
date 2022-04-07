""" My thought process to approach this problem was to consider all the possible
different ways that the cannibals and missionaries could be assembled at either bank
and getting into the boat. Then after each iteration of times the boat goes recurisvely
call back on the initial method to consider all factors again before the next.
Then after each iteration once the other bank1 is at 0"""


# creating arrays for the boat and each bank consisting of m missionaries and c cannibals
bank1 = {'c': 3, 'm': 3}
bank2 = {'c': 0, 'm': 0}
boat = {'c': 0, 'm': 0}

# printing each change to the banks with the number of cannibals and missionaires 
def printing(a, b, c):
    # initating way to format print statement 
    msg = """
    Bank 1: {} cannibals, {} missionaries
    Bank 2: {} cannibals, {} missionaries
    Boat: {} cannibals, {} missionaries
    """
    # inputing the current counts of people on each bank and in boat
    print(msg.format(a['c'], a['m'], b['c'], b['m'],
                     c['c'], c['m']))


def solveProblem(bank1, bank2, boat):
    # scenario if bank2 is empty
    if all(x == 0 for x in bank2.values()):
        printing(bank1, bank2, boat)
        #one cannibal leaves bank1 then goes on boat
        bank1['c'] -= 1
        boat['c'] += 1

    #one missionary leaves bank1 then goes on boat
    bank1['m'] -= 1
    boat['m'] += 1
    printing(bank1, bank2, boat)

    # scenario if bank1 is empty
    if all(x == 0 for x in bank1.values()):
        #one cannibal and one missionary go out of boat then both go on bank 2
        boat['c'], boat['m'] = 0, 0
        bank2['c'] += 1
        bank2['m'] += 1
        printing(bank1, bank2, boat)
        #we are done they crossed
        return

    #one missionary goes out of boat then goes on bank 2
    boat['m'] -= 1
    bank2['m'] += 1
    printing(bank1, bank2, boat)

    #one cannibal leaves bank1 and goes on boat
    bank1['c'] -= 1
    boat['c'] += 1
    printing(bank1, bank2, boat)

    #one cannibal goes out of boat then goes on bank 2
    boat['c'] -= 1
    bank2['c'] += 1
    printing(bank1, bank2, boat)

    #another series of crossings
    solveProblem(bank1, bank2, boat)

# calling cann_miss()
def main():
    solveProblem(bank1, bank2, boat)


if __name__ == '__main__':
    main()
