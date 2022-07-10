import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools

ntweets = input("Number of tweets to scrape: ")
search = input("Enter search term: ")
location= input("Enter location leave blank for all location: ")
if location == "":
    location = None
else:
    search = search + " near " + "{location}"

datef= input("Enter from date leave blank for all: ")
datet= input("Enter to date leave blank for all: ")

if datef!="":
    search = search + " since:" + datef
elif datet!="":
    search = search + " until:" + datet
elif datef != "" and datet != "":
    search = search + " since: {datef} until: {datet}"


    
# the scraped tweets, this is a generator
scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

# slicing the generator to keep only the first 100 tweets
sliced_scraped_tweets = itertools.islice(scraped_tweets, ntweets)

# convert to a DataFrame and keep only relevant columns
df = pd.DataFrame(sliced_scraped_tweets)[['date', 'content', 'lang']]
index_to_drop=df[df['lang'] != 'en'].index
df.drop(index_to_drop, inplace=True)
df.drop(['lang'], axis=1, inplace=True)
print(df.head())
csv_data= df.to_csv('tweets_df2.csv', index=False)

