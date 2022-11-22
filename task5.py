import matplotlib.pyplot as plt
import pandas as pd

def task5():
    review = pd.read_csv("task2.csv")
    
    # Group the reviews by their categories
    review_groupby = review.groupby("category")

    category = []
    avg_review = []
    
    # Adding in the corresponding average scores to the categories
    for i, j in review_groupby:
        category.append(i)
        avg_review.append(j["average_score"].mean())

    plt.figure(figsize = (30, 12), dpi = 80)
    plt.bar(category, avg_review, width=0.6)

    # Generating bar graph
    plt.xticks(rotation = 90, rotation_mode = "anchor", ha="right")
    plt.xlabel("Category", labelpad=20)
    plt.ylabel("average_score")
    plt.title("Average review scores of products under different categories")
    plt.savefig("task5.png", bbox_inches='tight')

    return None
