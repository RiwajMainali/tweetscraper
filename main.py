import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools

# creating search query
def create_search():
    ntweets = input("Number of tweets to scrape: ")
    search = input("Enter search term: ")
    location= input("Enter location leave blank for all location: ")
    if location == "":
        location = None
    else:
        search = search + " near:" + '"'+str(location)+'"'
    datef= input("Enter from date leave blank for all: ")
    datet= input("Enter to date leave blank for all: ")

    if datef != "" and datet != "":
        search = search + " since:"+datef+" until:"+datet
    elif datef!="":
        search = search + " since:" + datef
    elif datet!="":
        search = search + " until:" + datet
    return search, ntweets, datef, datet


search, ntweets, datef, datet = create_search()
print("'"+str(search)+"'")
tweets_list2 = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper( "'"+str(search)+"'").get_items()):
    if i>=int(ntweets):
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
tweets_df2.head()

# Export dataframe into a CSV
tweets_df2.to_csv('tweets_df2.csv', sep=',', index=False)
