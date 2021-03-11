import tweepy
import matplotlib.pyplot as plt
import os

from TwitterCredentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

user = api.me()

tweets = user.statuses_count
likes = user.favourites_count
following = user.friends_count

names = ['Tweets', 'Likes', 'Following']

values = [tweets,likes,following]

plt.bar(names, values, color = ['red', 'green', 'blue']) #colours of each bar
plt.suptitle("@%s's user stats" % user.screen_name) #title of the bar chart
plt.savefig('twitterStats.png') #saves figure as a .png file

image = "twitterStats.png"
status = "@%s's Twitter stats" % (user.screen_name)
api.update_with_media(image, status)

plt.show() #shows bar chart 

