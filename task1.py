import os
import pandas as pd
import json

def task1():
    data = pd.read_csv("/course/data/dataset.csv")
    
    # Generating dictionary to save output
    output = {}

    output["Number of Products:"] = len(set(data["ID"]))
    output["Number of Categories:"] = len(set(data["category"]))

    # Generate JSON file
    with open('task1.json', 'w') as file:
        json.dump(output,file, indent = 4)

    return None
