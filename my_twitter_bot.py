import tweepy, praw
import time
#from keys import * #File that stores API keys || Commented out for Heroku
from reddit_material import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

mentions = api.mentions_timeline()

# Where the last seen tweet is stored
TWITTER_ID_FILE = 'last_seen_id.txt'

# Retrieves the last seen id in the file last_seen_id.txt
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# Overwrites the current content with the given last seen id
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# Replies to tweets that have tweeted at me and include the hashtag #YNWA
def reply_to_tweets():
    print('Retrieving and replying...')
    last_seen_id = retrieve_last_seen_id(TWITTER_ID_FILE)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, TWITTER_ID_FILE)
        if '#ynwa' in mention.full_text.lower():
            print('Found a scouser!')
            print('Responding...')
            api.update_status('@' + mention.user.screen_name + ' ' +
                    'You\'ll never walk alone, my friend!', mention.id)

# Tweets out the title and comments
def post_title_and_comments(sub, numComments, contentFilter, timeFilter):
    api.update_status(most_x_title_comments(sub, numComments, contentFilter, timeFilter)[0:276] + '...')

# for some reason, all this seems not to work:

    # # If the tweet is longer than the length Twitter allows (280 characters), 
    # # it will reply to itself and create a thread
    # if len(most_x_title_comments(sub, numComments, contentFilter, timeFilter)) > 280:
    #     print('Too long, cutting it short...')
    #     api.update_status(most_x_title_comments(sub, numComments, contentFilter, timeFilter)[0:276] + '...')
    # else:
    # # If it is too long, post the first 280 characters and create a reply with the remaining
    # # ... this has yet to be implemented. At the moment, if it is too long, it will just tweet the
    # # first 280 characters.
    #     print('Not too long, posting...')
    #     api.update_status(most_x_title_comments(sub, numComments, contentFilter, timeFilter))

# Main function that calls the others

while True:
    print('-----------------------------------\n')
    print('Booting main while loop...')
    reply_to_tweets()
    
    post_title_and_comments('LiverpoolFC', 3, 'top', 'month')
    post_title_and_comments('soccer', 3, 'top', 'year')
    
    time.sleep(10)
