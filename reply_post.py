#!/usr/bin/python
import praw
import pdb
import re
import os
import time


# Create the Reddit instance
reddit = praw.Reddit('bot1')

y=0
x=0
n=30
while 1==1:
    print("NEW COMMENTS\n","\n")
    time.sleep(120)
    for comment in list(reddit.redditor("YoUaReSoHiLaRiOuS").comments.new(limit=50)):
        if comment.saved:
            print("saved comment title: ", comment.body, " subreddit: ", comment.subreddit, "\n")
            continue
        if "ha".lower() in comment.body.lower():
            try:
                comment.reply("Such a funny comment. r/unexpectedhilarity " "\n\n"  "---\n\n" "^(I am a bot. If this post was made by accident, please tell u/ Omegas_Bane. This is version 0.05 of Incredibly_Hilarious. For suggestions, go to r/unexpectedhilarity.)")
                comment.save()
                print("Comment number: ", y+1, "\n")
                print("Bot replying to : ", comment.author, "\n; Body: ", comment.body, "\n; in subreddit: ", comment.subreddit, "\n")
                y=y+1
            except Exception as e:
                print("\nEXCEPTION: ", e)
                print("\nbroken comment title: ", comment.body, " subreddit: ", comment.subreddit, "\n")
                pass
    y=0
    print("HOT COMMENTS\n","\n")
    time.sleep(120)
    for comment in list(reddit.redditor("YoUaReSoHiLaRiOuS").comments.hot(limit=n)):
        if comment.saved:
            print("saved comment title: ", comment.body, " subreddit: ", comment.subreddit, "\n")

            n=n+1
            if n >=100:
                n=30
            continue
        if "ha".lower() in comment.body.lower():
            try:
                comment.reply("Such a funny comment. r/unexpectedhilarity " "\n\n"  "---\n\n" "^(I am a bot. If this post was made bn accident, please tell u/ Omegas_Bane. This is version 0.05 of Incredibly_Hilarious. For suggestions, go to r/unexpectedhilarity.)")
                comment.save()
                print("Comment number: ", y+1, "\n")
                print("Bot replying to : ", comment.author, "\n; Body: ", comment.body, "\n; in subreddit: ", comment.subreddit,"\n")
                y=y+1
            except Exception as e:
                print("\nEXCEPTION: ", e)
                print("broken comment title: ", comment.body, " subreddit: ", comment.subreddit, "\n")
                pass
    y=0
    print("Master Iterations: ", x+1, "\n\n")
    x = x+1
