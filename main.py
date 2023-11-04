from web_scrape import Post, SubReddit
import time

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

if __name__ == "__main__":
    main()
