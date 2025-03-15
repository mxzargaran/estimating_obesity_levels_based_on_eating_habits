import math


def get_bmi(weight, height):
    return weight / (height**2)


def categorize_bmi(bmi):
    """Categorize BMI using definitions from https://www.sciencedirect.com/science/article/pii/S2352340919306985#sec2."""
    max_bmi_for_category = {
        18.5: "Insufficient_Weight",
        25: "Normal_Weight",
        30: "Overweight_Level_I",
        35: "Obesity_Type_I",
        40: "Obesity_Type_II",
        math.inf: "Obesity_Type_III",
    }
    for max_bmi, category in max_bmi_for_category.items():
        if bmi < max_bmi:
            return category
    msg = "Unable to categorize BMI"
    raise ValueError(msg)


def get_water_consumption_weight(water, weight):
    return water / weight
