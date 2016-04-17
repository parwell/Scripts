# finds breakdown of reddit karma for a user

import praw

user_agent = ("Karma breakdown by /u/OutOfTine")
r = praw.Reddit(user_agent=user_agent)
limit = 100
user_name = "OutOfTine"
user = r.get_redditor(user_name)
gen = user.get_submitted(limit=limit)
karmaBySubreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karmaBySubreddit[subreddit] = (karmaBySubreddit.get(subreddit, 0) + thing.score)

for key in karmaBySubreddit:
    print("Subreddit: " + key)
    print("Karma: " + str(karmaBySubreddit[key]) + "\n")

input()