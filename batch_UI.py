from load_data import *
from sort import *
from curve_fit import *
from histogram import *


commandFile = input(
    "Please enter the name of the file where your commands are stored: ")

batch_file = open(commandFile, 'r')

characters = []

for line in batch_file:
    items = line.strip().split(";")
    if items[0].lower() == "e":
        break
    elif items[0].lower() == "l":
        if items[2] == "All":
            characters = load_data(items[1], ("All", "N/A"))
            characters = calculate_health(characters)

        elif items[2] == "Strength":
            characters = load_data(items[1], (items[2], eval(items[3])))

        elif items[2] == "Luck":
            characters = load_data(items[1], (items[2], float(items[3])))

        else:
            characters = load_data(items[1], (items[2], items[3]))
            characters = calculate_health(characters)

        print("data loaded")

    elif items[0].lower() == "s":
        characters = sort(characters, items[2], items[1])
        print("data sorted")

        if items[3].lower() == "y":
            print(characters)

    elif items[0].lower() == "c":
        print(curve_fit(characters, items[1], int(items[2])))

    elif items[0].lower() == "h":
        histogram(characters, items[1])
