from web_scrape import Post, SubReddit
import mp3_maker
import mp4_maker
import time
import os
import random

SUB_REDDIT_URLS = [
    "https://www.reddit.com/r/AmItheAsshole/",
    "https://www.reddit.com/r/confession/",
    "https://www.reddit.com/r/offmychest/",
    "https://www.reddit.com/r/TrueOffMyChest/"
]


def main():
    # DO NOT UNCOMMENT UNTIL ITS READY TO RUN
    # for url in SUB_REDDIT_URLS:
    #     time.sleep(random.randint(1,3))
    #     subreddit = SubReddit(url)
    #     subreddit.export()
    # # pass

    # posts_path = os.getcwd() + "/posts"
    # posts_list = os.listdir(posts_path)

    # for e in posts_list:
    #     print(e)
    #     mp3_maker.mp3(posts_path + "/" + e)

    mp4_maker.export(os.getcwd() + "/mp3_files/" ,os.listdir(os.getcwd() + "/mp3_files"))

if __name__ == "__main__":
    main()
