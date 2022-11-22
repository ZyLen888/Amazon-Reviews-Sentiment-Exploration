# Amazon-Reviews-Sentiment-Exploration-
🎯 Goal: Identify positive and negative sentiments by analysing the linguistic patterns in the Amazon reviews.   

💻 Data Analysis work done in Python as school projects   

## ✅ Amazon Reviews Sentiment Exploration 

Websites such as Amazon contain large numbers of product reviews.  This presents a rich source of information that we can use to understand more about these products, as well as how people communicate positive and negative sentiments more generally.

In this assignment, you will be working on a dataset comprising reviews of more than 1000 products.

Using this dataset, you will have an opportunity to learn how to identify positive and negative sentiments by analysing the linguistic patterns in the reviews.

### Task 1: Loading data (1 mark)
Implement the function task1() in task1.py that outputs a json file called task1.json in the following format:
{"Number of Products:": X, "Number of Categories:": Y}
where X and Y  are the number of products and number of categories respectively. 

### Task 2: Data aggregation (3 marks)
Each review contains a review_star field allowing you to determine how many stars (out of a possible 5) the review rated the product.  For example, a 5 star review contains the following:

"review_star": "a-icon a-icon-star a-star-5 review-rating"
Implement the function task2() in task2.py which determines the average review score for each product.  Any review with a missing or invalid review_star field should not be included in the calculation.  If a product contains no valid reviews, you should assign it an average score of 0 or None.

Your function should save its output to a csv file called task2.csv, which contains the following headings: ID,  category, average_score. Each row in the file should contain the details of one product, with 

- ID and category containing the original values in the data file.
- average_score being the average review score for each product

The rows in task2.csv should be in ascending order of ID.

### Task 3: Calculating the average product price (2 marks)
Each product comes with a cost field, which specifies the sale price of the item. The format of this field is not consistent - some products have a single cost whereas others have a price range.

Implement the function task3() in task3.py that calculates the average cost for each product:

- If a product contains only a single price, that price should be the average cost.

- If a product contains a price range (e.g. $X - $Y), then the average cost should be (X+Y)/2

- If a product contains an invalid or missing price, then average cost should be zero.

All average costs should be listed as a single numeric figure, rounded to two decimal places, with no dollar signs present.

Your function should save its output to a csv file called task3.csv, which contains the following headings: ID, category, average_cost. Each row in the file should contain the details of one product, with

- ID and category containing the original values in the data file.

- average_cost being the average cost as determined above.

The rows in task3.csv should be in ascending order of ID.

### Task 4: Plotting the average review score (1 mark)
For this task, consider only the 'Pet Supplies' category of products.

Implement the function task4() in task4.py to generate a plot allowing you to compare the average price with the average review score for each product in 'Pet Supplies'.  Save your plot plot as task4.png.

### Task 5: Comparing the review scores between categories (1 mark)
Implement the function task5() in task5.py which outputs a file called task5.png comparing the means of the average review scores of products in each category.

### Task 6: Text processing (2 marks)
We would now like to develop a way of understanding whether a review is favourable or unfavourable towards a product, based on the text of the review.  To do this, we would like to consider each sequential pair of words in the product.  For example, intuitively if the sequence 'great product' appears in a review, we might conclude that the review is favourable to the product.  Building this type of system requires us to pre-process the text of the reviews.

The text content of a review is in the JSON formatted REVIEWLIST field's review_body value.

Implement the function task6() in task6.py that performs the following pre-processing steps on the content of the reviews:

1. Convert all non-alphabetic characters (for example, numbers, apostrophes and punctuation), except for spacing characters (for example, whitespaces, tabs and newlines) to single-space characters. For example, ‘&’ should be converted to ‘ ’. You should consider non-English alphabetic characters as non-alphabetic for the purposes of this conversion.

2. Convert all spacing characters such as tabs and newlines into single-space characters, and ensure that only one whitespace character exists between each token.

3. Change all uppercase characters to lowercase.

4. Remove all stop words in nltk’s list of English stop words from the review.

5. Remove all remaining words that are only one or two characters long from the review.

6. Generate each sequential pair of words that occur in the review (i.e. word bigrams without padding).  For example, the review 'great product great price' should generate the following list: ['great product', 'product great', 'great price']

Once steps 1 -- 6 are done, build a JSON file representing each review in the dataset.  The JSON file should contain a list of objects.  Each object should represent one review and contain the following key/value pairs:

- score: containing the score for that review

- bigrams: containing the list of word bigrams appearing in the review as described above

Any reviews that don't contain a valid score or contain no bigrams after pre-processing should be ignored.

Your file should be saved as task6.json. 

The creation of vocabulary should be implemented reasonably efficiently.  The run time of task 6 should be no more than 45 seconds. Excessively long execution time for this task will result in a deduction of up to 2 marks.

Note that you might want to use an output from a previous task for convenience, but this is not required.

### Task 7: Detecting the most indicative bigrams of positive reviews (4 marks)

#### What is a positive review? What is a negative review?
In the context of this dataset, we will consider only a 5-star review to be 'positive' and only a 1-star review to be 'negative'.  Based on this, you should be able to separate the reviews into two collections:

#### Odds ratio
In this task we wish to discover which bigrams are the most indicative of positive reviews.  We will consider the vocabulary as all bigrams that appear in a positive or negative review.

First, define the probability that a bigram bb in our vocabulary appears in a positive review.

![Image1](https://i.ibb.co/x7xq3fq/Screenshot-2022-11-22-at-4-14-19-PM.png)

Further, the odds that a bigram bb appears in a positive review is defined as

![Image2](https://i.ibb.co/87MznK3/Screenshot-2022-11-22-at-4-19-40-PM.png)

If you have done some probability, odds are an equivalent way of presenting a probability. Odds essentially compare the number of events that produce an outcome against the number that do not: the higher the probability, the higher the odds. An odds value greater than 1 indicates that the bigram bb is more likely to appear in a positive review than it is absent.

![Image3](https://i.ibb.co/KXkbbX9/Screenshot-2022-11-22-at-4-20-30-PM.png)

#### Your tasks:

Implement the function task7() in task7.py that does the following:

- Calculate the log_odds_ratio for each bigram in the vocabulary. 
- Exclude the bigrams where p_p or p_n is exactly 0 or 1 (bigrams that appear exclusively in positive reviews or negative reviews). 

With the remaining bigrams in the vocabulary:

- Output a csv file called task7a.csv with the following headings: bigram, log_odds_ratio. Each row should represent a bigram in the vocabulary and the log odds ratio for that bigram. The value of log_odds_ratio is to be rounded to 4 digit from the decimal point. The entries in task7a.csv should be in ascending order of log_odds_ratio.

- Output a file called task7b.png which contains an appropriately chosen graph showing the distribution of log_odds_ratio for bigrams in the vocabulary.

- Output a file called task7c.png which contains an appropriately chosen graph, showing the top 10 bigrams with the highest odds ratios, and the top 10 bigrams with the lowest odds ratios. 

### Task 8: Analysis Report (6 marks)
Write a brief report of no more than 500 words to summarise your analytical findings. You should incorporate the plots in tasks 4, 5 and 7 in your analysis and also include the following:

- A brief descriptions of the data sources and of the plots from tasks 4, 5 and 7. (0.5 mark)
- Comment relationship between review scores and average price based on task4.png. (0.5 mark)
- Your observations on the mean score for each category based on task5.png. (0.5 mark)
- Interpretation of the distribution of the log odds ratios for all bigrams as shown in the plot in task7 (task7b.png). (1 mark)
- The extent to which you agree or disagree with the “most indicative” bigrams for positive and negative reviews, as shown in task7c.png. (1 mark)
- A brief discussion of the limitations of this dataset, the processing techniques and what can be done in the future.' (1.5 mark)
- The report should be coherent, clear, and concise, and written in an appropriate language. (1 mark)
