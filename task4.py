import matplotlib.pyplot as plt
import pandas as pd

def task4():

    review = pd.read_csv("task2.csv")
    price = pd.read_csv("task3.csv")

    # Combining two datasets in order to generate plot with both attributes
    combined = review.merge(price, left_on = "ID", right_on = "ID")
    combined = combined.where(combined["category_x"] == "Amazon Devices & Accessories")

    # Generating a scatterplot
    plt.figure(figsize = (8, 6), dpi = 80)
    plt.scatter(combined["average_cost"], combined["average_score"])

    plt.xlabel("average_cost")
    plt.ylabel("average_score")
    plt.title("Comparison of the average price with average review score (Pet Supplies) ")
    plt.savefig("task4.png")

    return None
