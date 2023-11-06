from web_scrape import Post, SubReddit
import time
import os

SUB_REDDIT_URLS = [
    "https://www.reddit.com/r/AmItheAsshole/",
    "https://www.reddit.com/r/confession/",
    "https://www.reddit.com/r/offmychest/",
    "https://www.reddit.com/r/TrueOffMyChest/"
]


def main():
    # DO NOT UNCOMMENT UNTIL ITS READY TO RUN
    for url in SUB_REDDIT_URLS:
        time.sleep(2)
        subreddit = SubReddit(url)
        subreddit.export()
    # pass

    posts_path = os.getcwd() + "/posts"
    posts_list = os.listdir(posts_path)

    c = 0
    for e in posts_list:
        os.system("python3 mp3_maker.py -v en_us_001 -f " +  posts_path + "/" + e + " -n " + e + ".mp3")

if __name__ == "__main__":
    main()
