import load_data
import numpy as np
import matplotlib.pyplot as mp
import sort
import histogram
import curve_fit


key = []
ask_commands = True
open_file = False

while ask_commands == True:
    print("The available commands are:")
    print("    L)oad Data")
    print("    S)ort Data")
    print("    C)urve Fit")
    print("    H)istogram")
    print("    E)xit   ")

    user_input = input("Please type your command: ").upper()

    if user_input == "L":
        file_name = input("Please enter the name of the file: ")
        open_file = True

        while True:
            attribute = input(
                "Please enter the attribute to use as a filter: ")

            if attribute == "All":
                key = load_data.calculate_health(
                    load_data.load_data(file_name, (attribute, 0)))
                break

            elif attribute in ['Occupation', 'Weapon']:
                value = input("Please enter the value of the attribute: ")
                key = load_data.calculate_health(
                    load_data.load_data(file_name, (attribute, value)))
                break

            elif attribute == 'Strength':
                value = input("Please enter the value of the attribute: ")
                key = load_data.load_data(
                    file_name, (attribute, eval(value)))
                break

            elif attribute == 'Luck':
                value = input("Please enter the value of the attribute: ")
                key = load_data.load_data(
                    file_name, (attribute, float(value)))
                break

            else:
                print("Invalid Attribute")

        print("Data loaded")

    elif user_input == "S":
        if open_file == False:
            print("File not loaded. Please, load a file first.")
            continue
        attribute = input(
            "Please enter the attribute you want to use for sorting: 'Agility', 'Armor', 'Intelligence', 'Health' ")
        order = input("Ascending (A) or Descending (D) order: ").upper()
        display = input("Data Sorted. Do you want to display the data?: ")
        key = sort.sort(key, order, attribute)
        if display == "Y":
            print(key)
        else:
            pass

    elif user_input == "C":
        if open_file == False:
            print("File not loaded. Please, load a file first.")
            continue
        attribute = input(
            "Please enter the attribute you want to use to find the best fit for Health:")
        order = int(
            input("Please enter the order of the polynomial to be fitted: "))
        print(curve_fit.curve_fit(key, attribute, order))

    elif user_input == "H":
        if open_file == False:
            print("File not loaded. Please, load a file first.")
            continue
        attribute = input(
            "Please enter the attribute you want to use for plotting: ")
        histogram.histogram(key, attribute)

    elif user_input == "E":
        ask_commands = False

    else:
        if open_file == True:
            print("Invalid command")
        else:
            print("No such command")
