import matplotlib.pyplot as plt


def histogram(character_list: list[dict], attribute: str) -> float:
    """
    Return a histogram -1 if the attribute is categorical (e.g., Occupation) and the maximum value for the given attribute if it is numerical.Plot a histogram if attribute is numerical.

    >>>histogram([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}],'Health')
    62.71
    >>>histogram([{'Occupation': 'EB','Personality': 656.37}, {'Occupation': 'H', 'Personality': 12.71}],'Personality')
    656.37
    >>>histogram([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}],'Occupation')
    -1
    """

    dict1 = {}
    for i in range(0, len(character_list)):
        if character_list[i][attribute] not in dict1:
            dict1[character_list[i][attribute]] = 1
        else:
            dict1[character_list[i][attribute]] += 1
    list1 = list(dict1.keys())
    list2 = list(dict1.values())
    #print(list1, list2)
    fig1 = plt.figure()
    plt.title("Character Histogram of " + attribute)
    plt.xlabel(attribute)
    plt.ylabel("quantity")
    plt.bar(list1, list2)
    plt.show()
    if isinstance(list1[0], (int, float)):
        return max(list1)
    else:
        return -1


# Do NOT include a main script in your submission

