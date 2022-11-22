import json
import pandas as pd
import nltk
from collections import defaultdict
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.util import ngrams
import re

# source code from workshop
def bigrams(text):
    """
    computes bigrams (2-grams) given a tokenized text
    """
    return ngrams(text.split(), 2)

def task6():

    json_list = []
    data = pd.read_csv("/course/data/dataset.csv") 

    for i, row in data.iterrows():
        p_review = row["REVIEWLIST"]
        p_review = json.loads(p_review)

        # Extract review rating and the review body text 
        for review in p_review:
            review_dictionary = {}
            if review["review_star"]:
                rating = re.search("\d", review["review_star"]).group()
            body = review["review_body"]
            
            # Defining a pattern that filters out non-alphabetical characters
            nonalpha_pattern = r'[^A-Za-z]'
            clean = re.sub(nonalpha_pattern, ' ', body, flags = re.IGNORECASE)
            clean = clean.split() 
            clean = " ".join(clean)
            clean = clean.lower()
            
            stop_words = list(set(stopwords.words('english')))
            
            # Removing stop words
            word_list = [word for word in clean.split() if not word in stop_words]

            # Removing words that are one or two characters long
            word_list = [word for word in word_list if len(word) > 2]

            clean_text = " ".join(word_list)
            bi_gram = bigrams(clean_text)
            
            bigram_result = [" ".join([a,b]) for a, b in bi_gram]

            review_dictionary["score"] = rating
            review_dictionary["bigrams"] = bigram_result

            json_list.append(review_dictionary)

    with open('task6.json', 'w') as file:
        json.dump(json_list,file)
        
    return None
