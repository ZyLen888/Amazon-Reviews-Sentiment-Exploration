import json
import pandas as pd
import re

def convert_price(result):
    """
    This function converts the price string to float without special characters 
    for ease of manipulation.
    """
    # 1. missing value or invalid value (without $ sign)
    if len(result) == 0:
        return 0
    # 2. Single value
    elif len(result) == 1:
        return round(float(result[0][1:]), 2)
    # 3. Range value
    else:
        return round((float(result[0][1:]) + float(result[1][1:]))/2, 2)

def task3():

    data = pd.read_csv("/course/data/dataset.csv")

    p_id_list = []
    p_category_list = []
    p_avg_cost = []

    # Defining the pattern to search for price
    pattern = r'\$\d*\.\d\d'

    for i, row in data.iterrows():

        p_id = row["ID"]
        p_category = row["category"]

        result = re.findall(pattern, row["cost"])

        price = convert_price(result)

        p_id_list.append(p_id)
        p_category_list.append(p_category)
        p_avg_cost.append(price)

    task3_df = pd.DataFrame({"ID": p_id_list, "category" : p_category_list, "average_cost": p_avg_cost})

    task3_df.to_csv("task3.csv", index = False)

    return None


    
