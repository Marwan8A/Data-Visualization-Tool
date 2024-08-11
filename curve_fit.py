import numpy as np
import matplotlib.pyplot as plt

def curve_fit(dict_list: list, attribute: str, degree: int) -> str:
    """
    Return the equation for the curve of best fit, based on the graph of average health vs another attribute and the degree of polynomial given.
    Preconditions: 1 <= degree <= 5, attribute != "Occupation"
    >>>curve_fit([{"Health": 42,"Strength": 13}, {"Health": 31,"Strength": 5}, {"Health": 79,"Strength": 26}, {"Health": 24, "Strength": 26}], "Strength", 2)
    'y = -0.030677655677655808x^2 + 1.9271978021978078x + 22.130952380952365'
    >>>curve_fit([{"Health": 42,"Strength": 13}, {"Health": 24, "Strength": 26}], "Strength", 5)
    'y = -1.3846153846153826x + 59.999999999999964'
    """
    d = {}
    for i in range(len(dict_list)):
        if d.get(dict_list[i].get(attribute)):
            d[dict_list[i].get(attribute)] = (dict_list[i].pop("Health") + d.get(dict_list[i].get(attribute))) / 2
        else:
            d[dict_list[i].get(attribute)] = dict_list[i].pop("Health")
    average_health_list = []
    attrib_list = []   
    for i in d:
        attrib_list.append(i)
        average_health_list.append(d[i])
    if degree < len(dict_list):
        x = attrib_list
        y = average_health_list
        coef = np.polyfit(x, y, degree)
        polynomial = "y = "
        for i in range(0, len(coef), 1):
            if i == len(coef) - 2:
                polynomial = polynomial + str(coef[i]) + "x + "
            elif i == len(coef) - 1:
                polynomial = polynomial + str(coef[i])
            else:
                polynomial = polynomial + str(coef[i]) + "x^" + str(degree - i) + " + "
        return polynomial       
    else:
        x = attrib_list
        y = average_health_list
        coef = np.polyfit(x, y, len(dict_list) - 1)    
        polynomial = "y = "
        for i in range(0, len(coef), 1):
            if i == len(coef) - 2:
                polynomial = polynomial + str(coef[i]) + "x + "
            elif i == len(coef) - 1:
                polynomial = polynomial + str(coef[i])
            else:
                polynomial = polynomial + str(coef[i]) + "x^" + str(degree - i) + " + "
        return polynomial

# Do NOT include a main script in your submission



