import tweepy
import time
from keys import * #File that stores API keys

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

mentions = api.mentions_timeline()

FILE_NAME = 'last_seen_id.txt'

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

def reply_to_tweets():
    print('booted function...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#ynwa' in mention.full_text.lower():
            print('Found a scouser!')
            print('Responding...')
            api.update_status('@' + mention.user.screen_name + ' ' +
                    'You\'ll never walk alone, my friend!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(10)