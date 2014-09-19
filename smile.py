from twitterapi import api, debuguser
import twitter
import random

debug = True

followers = api.GetFollowers()
current = random.randint(0, len(followers) - 1)
print followers[current].GetScreenName()

lines = open('phrases').read().splitlines()
myline = random.choice(lines)

if debug:
    api.PostUpdate("@" + debuguser + " current user is " + followers[current].GetScreenName() + " phrase: " + myline)

else:
    api.PostUpdate("@" + followers[current].GetScreenName() + " " + myline)
