import praw

reddit = praw.Reddit(client_id = "DYOOxWfsW80nfw", client_secret = "rXiv94kuOoI4BL3BPrBPq4O4glo", user_agent = "RedditScrapping")


import pandas as pd



def get_deta_from_subreddit(sub):
    posts = []
    try:
        ml_subreddit = reddit.subreddit(sub)
        for post in ml_subreddit.hot(limit=3000):
            posts.append(
                [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    except:
        print(sub + "gave error")
        return posts
    return posts

subreddits = ['downsyndrome','CompulsiveSkinPicking','bulimia','BPD']

all_posts = []
for subreddit in subreddits:
    print(subreddit)
    all_posts.extend(get_deta_from_subreddit(subreddit))
    print("size of posts:"+str(len(all_posts)))

all_posts = pd.DataFrame(all_posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
all_posts.to_excel("subreddits_downsyndrome.xlsx")