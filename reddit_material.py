import praw
from reddit_info import *

SUBREDDIT_TO_BROWSE = 'LiverpoolFC'
LIMIT = 10
REDDIT_IDS_FILE = 'id_posted.txt'

# Adding username and password allows for account-related actions
# (such as voting, reporting, etc.)
reddit = praw.Reddit(client_id= CLIENT_ID,
                     client_secret= CLIENT_SECRET,
                     user_agent= USER_AGENT,
                     username= USERNAME,
                     password= PASSWORD)
#subreddit = reddit.subreddit(SUBREDDIT_TO_BROWSE)

#### Okay, what do I want to do?
# I want a twitter bot that will tweet out the most 
# controversial/hot/top/new post with its top x comments

# The title and top x comments of top sorted submission (optional) with filter (optional)
def most_x_title_comments(sub, numComments, sortType="controversial", time_filter='day'):
    if sortType.lower() == "controversial":
        list_most_x = list(reddit.subreddit(sub).controversial(time_filter))
    elif sortType.lower() == "hot":
        list_most_x = list(reddit.subreddit(sub).hot())
    elif sortType.lower() == "top":
        list_most_x = list(reddit.subreddit(sub).top(time_filter))
    elif sortType.lower() == "new":
        list_most_x = list(reddit.subreddit(sub).new())
    else:
        print('ERROR: Sorting not specified')
        return 'ERROR: Sorting not specified'        
    
    most_x_post = use_post(list_most_x, list_most_x, REDDIT_IDS_FILE)
    
    list_most_x_comments = list(most_x_post.comments)
    comment_count = 0

    # For viewing purposes in terminal
    if sortType.lower() == "controversial":
        print('Posting title of most controversial submission of the {} from {}'.format(time_filter, most_x_post.subreddit._path))
        answer = 'Most controversial post of the {c}: {a} ({b})'.format(c=time_filter, a=most_x_post.title, b=most_x_post.url) + '\nIts top comment(s):\n'
    elif sortType.lower() == "hot":
        print('Posting title of hottest submission of the {} from {}'.format(time_filter, most_x_post.subreddit._path))
        answer = 'Hottest post: {a} ({b})'.format(a=most_x_post.title, b=most_x_post.url) + '\nIts top comment(s):\n'
    elif sortType.lower() == "top":
        print('Posting title of top submission of the {} from {}'.format(time_filter, most_x_post.subreddit._path))
        answer = 'Top post of the {c}: {a} ({b})'.format(c=time_filter, a=most_x_post.title, b=most_x_post.url) + '\nIts top comment(s):\n'
    elif sortType.lower() == "new":
        print('Posting title of newest submission of the {} from {}'.format(time_filter, most_x_post.subreddit._path))
        answer = 'Newest post (at time posted): {a} ({b})'.format(a=most_x_post.title, b=most_x_post.url) + '\nIts top comment(s):\n'
    
    for comment in list_most_x_comments[:numComments]:
        comment_count += 1
        answer += '#{a}: {b}'.format(a=comment_count, b=comment.body) + '\n'
        print('posted comment #{} of this post'.format(comment_count))
    return answer

# used_list: [List-of posts] File -> Post
# Determines if the first post's id is in the file, if it isn't, uses the 
# post and stores the id, if it is, recurs on the rest
def use_post(list_of_posts, same_list_tracking, file_name):
    # This list_of_ids is used to track the post number in the given list.
    # This is ancillary and helps to identify the post in the terminal.
    list_of_ids = [post.id for post in same_list_tracking]

    if not id_in_file(list_of_posts[0].id, file_name):
        store_new_reddit_id(list_of_posts[0].id, file_name)
        most_x_post = list_of_posts[0]
        print('Using post #{a} in list of posts (post id: {b})'.format(a=str(int(list_of_ids.index(most_x_post.id))+1), b=most_x_post.id))
        return most_x_post
    else:
        print('Skipping post, continuing to next...')
        return use_post(list_of_posts[1:], same_list_tracking, file_name)
        
# Produces a list with the ids of the posts that have already been posted
def retrieve_stored_reddit_ids(file_name):
    with open(file_name, 'r') as f_read:
        post_id_list = f_read.read().strip().split('\n')
    return post_id_list

# Adds the post id to the file of ids
def store_new_reddit_id(new_post_id, file_name):
    with open(file_name, 'a') as f_write:
        f_write.write('\n' + str(new_post_id))
    return

# Determines if a given id is in the file
def id_in_file(id, file_name):
    return str(id) in retrieve_stored_reddit_ids(file_name)
