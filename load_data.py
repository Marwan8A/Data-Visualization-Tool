import csv


def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """
    Returns the the list of characters stored as a dictionary whose occupation is provided as the input parameter.

    Precondition: the character being called has to exist in the file

    Examples:
    >>>character_occupation_list("characters-mat.csv",'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}...
    >>>character_occupation_list("characters-mat.csv",'DB')
    [{'Strength': 17, 'Agility': 5, 'Stamina': 10, 'Personality': 11, 'Intelligence': 11, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Club'} ...
    """

    in_file = open(file_name, 'r')
    occupation_list = []
    first_line = True
    count = 0

    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line

        else:
            if line[0] == occupation:
                character = {}
                character[table_header[1]] = int(line[1])
                character[table_header[2]] = int(line[2])
                character[table_header[3]] = int(line[3])
                character[table_header[4]] = int(line[4])
                character[table_header[5]] = int(line[5])
                character[table_header[6]] = float(line[6])
                character[table_header[7]] = int(line[7])
                character[table_header[8]] = line[8]
                occupation_list.append(character)
    in_file.close()
    return (occupation_list)


#==========================================#
# Place your character_strength_list function after this line


def character_strength_list(file_name: str, strength_range: tuple) -> list:
    """ This function will return a list of dictionaries which correspond to characters' attributes for characters with a strength between the given strength range in the tuple

    precondition: none

    >>> character_strength_list ('characters-mat.csv', (8, 11))
    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}, {another element}, …
    >>> character_strength_list ('characters-mat.csv', (1000, 10001))
    []
    """
    character_list = []
    in_file = open(file_name, 'r')
    first_line = True

    for line in in_file:
        line = line.strip().split(',')

        if first_line:
            first_line = False
            table_header = line

        elif int(line[1]) >= int(strength_range[0]) and int(line[1]) <= int(strength_range[1]):
            character = {}
            character[table_header[0]] = line[0]
            character[table_header[2]] = int(line[2])
            character[table_header[3]] = int(line[3])
            character[table_header[4]] = int(line[4])
            character[table_header[5]] = int(line[5])
            character[table_header[6]] = float(line[6])
            character[table_header[7]] = int(line[7])
            character[table_header[8]] = line[8]
            character_list += [character]

    in_file.close()
    return character_list
#==========================================#
# Place your character_luck_list function after this line


def character_luck_list(file_name: str, luck_stat: float) -> list:
    """
    Return the dictionaries of all characters from a data file
    that have a lower luck stat than the given luck in a list.
    >>> character_luck_list ('characters-mat.csv', 0.4)
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
    'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'},
    {'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9,
    'Personality': 10, 'Intelligence': 12, 'Armor': 10, 'Weapon': 'Dagger'},
    {another element}]
    >>> character_luck_list ('characters-mat.csv', 0.1)
    [] 
    """
    in_file = open(file_name, 'r')
    first_line = True
    character_loading_list = []
    character_list = []
    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            character = {}
            character[table_header[0]] = line[0]
            character[table_header[1]] = int(line[1])
            character[table_header[2]] = int(line[2])
            character[table_header[3]] = int(line[3])
            character[table_header[4]] = int(line[4])
            character[table_header[5]] = int(line[5])
            character[table_header[6]] = float(line[6])
            character[table_header[7]] = int(line[7])
            character[table_header[8]] = line[8]
            if character.pop('Luck') < luck_stat:
                character_list.append(character)
    return character_list

#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(file_name: str, weapon: str) -> list[dict]:
    """
    Return the list of characters (stored as a dictionary) whose weapon is provided as the input parameters.

    >>>character_weapon_list ('characters-mat.csv', 'Staff')
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},{another element},...]

    >>> character_weapon_list ('characters-mat.csv','aaa')
    []
    """
    in_file = open(file_name, 'r')
    first_line = True
    characters_list = []
    for line in in_file:
        line = line.strip()
        # line = line.lower()
        line = line.split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            character = {}
            character[table_header[0]] = line[0]
            character[table_header[1]] = int(line[1])
            character[table_header[2]] = int(line[2])
            character[table_header[3]] = int(line[3])
            character[table_header[4]] = int(line[4])
            character[table_header[5]] = int(line[5])
            character[table_header[6]] = float(line[6])
            character[table_header[7]] = int(line[7])
            character[table_header[8]] = line[8]
            characters_list.append(character)

    weapon_list = []
    for i in characters_list:
        if i[table_header[8]] == weapon:
            i.pop('Weapon')
            weapon_list.append(i)
    in_file.close()
    return weapon_list


#==========================================#
# Place your load_data function after this line

def load_data(file_name: str, filters: tuple) -> list[dict]:
    """
    Returns as a list of characters (stored as a dictionary) where the keys of the dictionary are the labels for all attributes in the spreadsheet except for the attribute in the first item of the tuple. If the first item of the tuple is invalid, the function will print the error message “Invalid Value” and return an empty list.
    >>> load_data('characters-mat.csv', ('Weapon', 'Staff'))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},{another element},…]
    >>>load_data('characters-mat.csv', ('All',-1))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8,'Weapon': 'Staff'},{another element},…]
    
    """
    in_file = open(file_name, 'r')
    first_line = True
    characters_list = []
    for line in in_file:
        line = line.strip()
        # line = line.lower()
        line = line.split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            character = {}
            character[table_header[0]] = line[0]
            character[table_header[1]] = int(line[1])
            character[table_header[2]] = int(line[2])
            character[table_header[3]] = int(line[3])
            character[table_header[4]] = int(line[4])
            character[table_header[5]] = int(line[5])
            character[table_header[6]] = float(line[6])
            character[table_header[7]] = int(line[7])
            character[table_header[8]] = line[8]
            characters_list.append(character)

    if filters[0] == 'All':
        return characters_list
    elif filters[0] == 'Weapon':
        return character_weapon_list(file_name, filters[1])
    elif filters[0] == 'Strength':
        return character_strength_list(file_name, filters[1])
    elif filters[0] == 'Luck':
        return character_luck_list(file_name, filters[1])
    elif filters[0] == 'Occupation':
        return character_occupation_list(file_name, filters[1])
    else:
        return 'Invalid Value', []
#==========================================#
# Place your calculate_health function after this line

def calculate_health(character_list: list) -> list:
    for character in character_list:
        health = (character['Strength'] + character['Agility'] + character['Stamina'] +
                  character['Personality'] + character['Intelligence'] + (character['Armor']**2*character['Luck']))
        character['Health'] = health

    return character_list

# Do NOT include a main script in your submission