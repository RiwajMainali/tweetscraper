import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools

# our search term, using syntax for Twitter's Advanced Search
search = input("Enter search term: ")
date= input("Enter date press nil for all dates: ")
location= input("Enter location press nil for all location: ")
if location == "nil":
    location = None
if date == "nil":
    date = None
    
# the scraped tweets, this is a generator
scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

# slicing the generator to keep only the first 100 tweets
sliced_scraped_tweets = itertools.islice(scraped_tweets, 100)

# convert to a DataFrame and keep only relevant columns
df = pd.DataFrame(sliced_scraped_tweets)[['date', 'content']]
print(df.head())
csv_data= df.to_csv('tweets_df2.csv', index=False)

