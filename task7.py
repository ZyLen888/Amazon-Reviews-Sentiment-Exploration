import collections
import math
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json

def task7():
    
    with open('task6.json', 'r') as file:
        reviews = json.load(file)

        positive = []
        negative = []

        for review in reviews:
            if review["score"] == str(5):
                positive.append(review["bigrams"])
            elif review["score"] == str(1):
                negative.append(review["bigrams"])
        
        # Count the number of positive and negative reviews
        positive_num = len(positive)
        negative_num = len(negative)

        # Joining all the positive and negative reviews into a single list
        positive = sum(positive, [])
        negative = sum(negative, [])

        # Count the number of total positive and negative reviews
        positive_counter = collections.Counter(positive)
        negative_counter = collections.Counter(negative)

        # Calculating probability for positive reviews
        positive_prob = {key: (value / positive_num) for key, value in positive_counter.items() if ((value / positive_num) != 0 or (value / positive_num) != 1)}
        
        # Calculating probability for negative reviews
        negative_prob = {key: (value / positive_num) for key, value in negative_counter.items() if ((value / negative_num) != 0 or (value / negative_num) != 1)}

        # Calculating odds for positive reviews
        odds_positive = {key: (prob / (1-prob)) for key, prob in positive_prob.items()}

        # Calculating dds for negative reviews
        odds_negative = {key: (prob / (1-prob)) for key, prob in negative_prob.items()}

        # Calculating odds ratio
        odds_ratio = {}


        # Adding in the bigrams that belong to both positive and negative reviews 
        keyset = set([key for key in odds_positive.keys()] + [key for key in odds_negative.keys()])
        for key in keyset:
            if (key not in odds_positive.keys()) or (key not in odds_negative.keys()):
                pass
            else:
                try:
                    odds_ratio[key] = odds_positive[key] / odds_negative[key]
                except ZeroDivisionError:
                    odds_ratio[key] = 0

        #log transformation of odds ratio (round to 4 digits)
        log_trans = {}

        for key, ratio in odds_ratio.items():
            if ratio == 0:
                log_trans[key] = 0
            else:
                log_trans[key] =round(math.log10(ratio), 4)

        # task7a
        task7a = pd.DataFrame({"bigram": log_trans.keys(), "log_odds_ratio": log_trans.values()})
        task7a = task7a.sort_values(by = "log_odds_ratio")
        task7a.to_csv("task7a.csv", index=False)

        # task7b
        sns.distplot(task7a["log_odds_ratio"], color = "lightgreen", label = "log_odds_ratio")
        plt.xlabel("log odds ratio")
        plt.ylabel("Density")
        plt.title("Distribution of the log odds ratio")
        plt.tight_layout()
        plt.savefig('task7b.png')

        # task7c
        asc = task7a.sort_values("log_odds_ratio")[:10]
        dsc = task7a.sort_values("log_odds_ratio", ascending = False)[:10]

        fig, axs = plt.subplots(2, figsize = (20,14))
        fig.suptitle('Odds ratios ranking')
        axs[1].bar(asc["bigram"], asc["log_odds_ratio"])
        axs[0].bar(dsc["bigram"], dsc["log_odds_ratio"])
        axs[1].set_xticklabels(asc["bigram"], rotation = 45)
        axs[1].set_title("Top 10 bigrams with the lowest odds ratios")
        axs[0].set_xticklabels(dsc["bigram"], rotation = 45)
        axs[0].set_title("Top 10 bigrams with the highest odds ratios")
        plt.tight_layout(h_pad = 5)
        plt.savefig("task7c.png")

    return None
