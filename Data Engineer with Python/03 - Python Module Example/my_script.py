from collections import Counter

# Import local package
import text_analyzer

word_counts = [Counter({'AutoML': 1,
          'DataCamp': 1,
          'H': 2,
          'In': 1,
          'Introduction': 1,
          'O': 2,
          'a': 1,
          'about': 1,
          'and': 1,
          'auto': 1,
          'glimpse': 1,
          'have': 1,
          'its': 1,
          'learn': 1,
          'of': 1,
          'this': 1,
          'to': 1,
          'tutorial': 1,
          'will': 1,
          'you': 1}),
 Counter({'DataCamp': 1,
          'Hacking': 1,
          'Learn': 1,
          'Significance': 1,
          'Stocks': 1,
          'Testing': 1,
          'and': 1,
          'co': 1,
          'data': 1,
          'how': 1,
          'manipulate': 1,
          'p': 1,
          'pandas': 1,
          'series': 1,
          'time': 1,
          'to': 1,
          'with': 1})]

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)
print(word_count_totals)

# Plot word_count_totals using plot_counter from text_analyzer
top_5_items = text_analyzer.plot_counter(word_count_totals)
print(top_5_items)

# Create an instance of Document with datacamp_tweet
datacamp_tweet = 'Basic linear regression example. #DataCamp #DataScience #Python #sklearn'
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)

# create a new document instance from datacamp_tweets
datacamp_tweets = '[DataCamp] Introduction to H2O AutoML --> In this tutorial, you will learn about H2O and have a glimpse of its auto…\n[DataCamp] Stocks, Significance Testing & p-Hacking --> Learn how to manipulate time series data with pandas and co…\nRT @cbismuth: Linear regression example with most significant features detection. #DataCamp #DataScience #Python #sklearn …\nLinear regression example with most significant features detection. #DataCamp #DataScience #Python #sklearn\nBasic linear regression example. #DataCamp #DataScience #Python #sklearn\nRT @David_Makinde_: I just completed Introduction to Python for Data Science \n#Datacamp\n#DataScience \n#Python\n[DataCamp] Enter the #DataFramedChallenge for a chance to be on an upcoming podcast segment. --> DataCamp has a pod…\n[DataCamp] Introduction to Python Metaclasses --> In this tutorial, you\'ll learn about metaclasses in Python. by De…\nI just completed Introduction to Python for Data Science \n#Datacamp\n#DataScience \n#Python\nRT @cbismuth: My pretty first classifier! #DataCamp #Python #sklearn\nMy pretty first classifier! #DataCamp #Python #sklearn\nRT @ascentt: The different #DataScience roles on the job market.'
datacamp_doc = text_analyzer.Document(datacamp_tweets)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.text)
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc.word_counts.most_common(5))


# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most most mentioned users
print(dc_tweets.mention_counts.most_common(5))


# Try the tweets thing
dc_tweets = text_analyzer.Tweets(datacamp_tweets)
print(dc_tweets.retweets.hashtag_counts)



