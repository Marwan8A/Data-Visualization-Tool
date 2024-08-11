def sort_characters_agility_bubble(characters: list[dict], direction: str) -> list[dict]:
    """This function takes a list of dictionaries representing characters and sorts them by the 'Agility' key if present for all characters in a specified order

    >>> sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'EB', 'Strength': 10}], 'A')
    Agility is not a key in the dictionary
    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'EB', 'Strength': 10}]
    >>> sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'EB', 'Agility': 10}], 'A')
    [{'Occupation': 'EB', 'Agility': 10}, {'Occupation': 'EB', 'Agility': 13}]
    >>> sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 10}, {'Occupation': 'EB', 'Agility': 13}], 'D')
    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'EB', 'Agility': 10}]
    """
    try:
        for x in range(len(characters)):
            characters[x]['Agility'] = characters[x]['Agility']

    except:
        print('Agility is not a key in the dictionary')
        return characters

    try:
        if direction == 'A':
            for x in range(len(characters) - 1):
                for i in range(len(characters) - 1):
                    if characters[i]['Agility'] > characters[i + 1]['Agility']:
                        temp = characters[i]
                        characters[i] = characters[i + 1]
                        characters[i + 1] = temp

            return characters

        elif direction == 'D':
            for x in range(len(characters) - 1):
                for i in range(len(characters) - 1):
                    if characters[i]['Agility'] < characters[i + 1]['Agility']:
                        temp = characters[i]
                        characters[i] = characters[i + 1]
                        characters[i + 1] = temp

            return characters

    except:
        return 'Something went wrong'

#==========================================#
# Place your sort_characters_intelligence_selection function after this line


def sort_characters_intelligence_selection(listo: list, sort_type: str) -> list:
    """
    Return a sorted list of characters based on intelligence unless the intelligence key is not present, then return the original list.
    Examples:
    >>> sort_characters_intelligence_selection([{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB', 'Intelligence': 9}]
    >>>sort_characters_intelligence_selection([{'Occupation':'EB'}, {'Occupation': 'M'}], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    """
    while True:
        if sort_type == "A":
            for dic in listo:
                value_1 = False
                for key in dic:
                    if key == "Intelligence":
                        value_1 = True
                if value_1 == False:
                    print("The ""Intelligence"" key is not present")
                    return listo
            for i in range(len(listo)):
                min_idx = i
                for j in range(i + 1, len(listo)):
                    for key in listo[j]:
                        if key == "Intelligence":
                            value_1 = listo[j].get(key)
                    for key in listo[min_idx]:
                        if key == "Intelligence":
                            value_2 = listo[min_idx].get(key)
                    if value_2 > value_1:
                        #min_idx = listo[j]
                        min_idx = j
                listo[i], listo[min_idx] = listo[min_idx], listo[i]
            return listo
        elif sort_type == "D":
            for dic in listo:
                value_1 = False
                for key in dic:
                    if key == "Intelligence":
                        value_1 = True
                if value_1 == False:
                    print("The ""Intelligence"" key is not present")
                    return listo
            for i in range(len(listo)):
                max_idx = i
                for j in range(i + 1, len(listo)):
                    for key in listo[j]:
                        if key == "Intelligence":
                            value_1 = listo[j].get(key)
                    for key in listo[max_idx]:
                        if key == "Intelligence":
                            value_2 = listo[max_idx].get(key)
                    if value_2 < value_1:
                        #max_idx = listo[j]
                        max_idx = j
                listo[i], listo[max_idx] = listo[max_idx], listo[i]
            return listo
        else:
            print("Invalid input, please try again.")

#==========================================#
# Place your sort_characters_health_insertion function after this line


def sort_characters_health_insertion(character_list: list[dict], order: str):
    """
    Return list sorted by 'Health',If “Health” is a key in the dictionary.Else, print a message stating the key is not in the dictionary.
    >>> sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health':62.71}]
    >>>sort_characters_health_insertion([{'Occupation':'EB'},{'Occupation': 'M'}], "A")
    "Health" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    >>>sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "D")
    [{'Occupation': 'H', 'Health': 62.71}, {'Occupation': 'EB', 'Health': 62.37}]

    """
    try:
        if order == 'A':
            for i in range(1, len(character_list)):
                a = character_list[i]
                key = a['Health']
                j = i - 1
                while j >= 0 and key < character_list[j]['Health']:
                    character_list[j + 1] = character_list[j]
                    character_list[j] = a
                    j -= 1
                    c = character_list[j + 1]
                    c['Health'] = key
            return character_list
        elif order == "D":
            for i in range(1, len(character_list)):
                a = character_list[i]
                key = a['Health']
                j = i - 1
                while j >= 0 and key > character_list[j]['Health']:
                    character_list[j + 1] = character_list[j]
                    character_list[j] = a
                    j -= 1
                    c = character_list[j + 1]
                    c['Health'] = key
            return character_list

    except:
        KeyError
        print('The key is not in the dictionary')
        return character_list

#==========================================#
# Place your sort_characters_armor_bubble function after this line


def sort_characters_armor_bubble(arr: list, order: str) -> list:
    """
    The function uses the bubble sorting algorithm to sort the list of
    character dictionaries. The parameter "arr" is a list of dictionaries, while
    the parameter "order" is a string where it can be specified if if should be
    ascending or descending order.
    Precondition: the parameter arr must be a list of dictionaries;
    and the parameter order must be 'A' or 'D'.

    Examples:

    >>> sort_characters_armor_bubble([{'Occupation': 'EB','Armor': 11}, 
    {'Occupation': 'H', 'Armor': 10}], "A")
    [{'Occupation': 'H', 'Armor': 10}, {'Occupation': 'EB', 'Armor': 11}]

    >>> sort_characters_armor_bubble([{'Occupation': 'EB','Armor': 11},
    {'Occupation': 'H', 'Armor': 10}], "D")
    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]

    >>> sort_characters_armor_bubble([{'Occupation': 'EB'}, 
    {'Occupation': 'M'}], "D")
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]

    """

    swap = True

    for i in range(len(arr) - 1):

        if "Armor" not in arr[i]:
            print(" 'Armor' key is not present. ")
            return arr

        while swap:
            swap = False
            for j in range(len(arr) - 1 - i):
                if order == "A":
                    if arr[j]["Armor"] > arr[j + 1]["Armor"]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swap = True

                if order == "D":
                    if arr[j]["Armor"] < arr[j + 1]["Armor"]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swap = True

    return arr

#==========================================#
# Place your sort function after this line


def sort(characters: list[dict], direction: str, sort_by: str) -> list[dict]:
    try:
        if sort_by == 'Agility':
            sort_characters_agility_bubble(characters, direction)

        elif sort_by == 'Intelligence':
            sort_characters_intelligence_selection(characters, direction)

        elif sort_by == 'Health':
            sort_characters_health_insertion(characters, direction)

        elif sort_by == 'Armor':
            sort_characters_armor_bubble(characters, direction)

        else:
            print('Cannot be sorted by', sort_by)

        return characters

    except:
        print('An error occured')

# Do NOT include a main script in your submission
