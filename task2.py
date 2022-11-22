import json
import pandas as pd
import re

def task2():

    data = pd.read_csv("/course/data/dataset.csv")
    p_id_list = []
    p_category_list = []
    p_review_score = []

    # Iterate through reviews in data
    for i, row in data.iterrows():
        p_id = row["ID"]
        p_category = row["category"]
        p_review = row["REVIEWLIST"]

        p_review = json.loads(p_review)
        total_rating = 0
        total_review = 0

        # Iterate through review rating and summing up all rating and number of reviews
        for review in p_review:
            if review["review_star"]:
                rating = re.search("\d", review["review_star"]).group()
                total_rating += int(rating)
                total_review += 1
        
        p_id_list.append(p_id) 
        p_category_list.append(p_category)

        if total_review > 0:
            p_review_score.append(total_rating / total_review)
        else:
            p_review_score.append(0)

        task2_df = pd.DataFrame({"ID": p_id_list, "category" : p_category_list, "average_score": p_review_score})

    task2_df.sort_values(by = ["ID"])

    # Generate CSV
    task2_df.to_csv("task2.csv", index = False)

    return None
