from web_scrape import Post, SubReddit

SUB_REDDIT_URLS = [
    "https://www.reddit.com/r/AmItheAsshole/",
    "https://www.reddit.com/r/confession/",
    "https://www.reddit.com/r/offmychest/",
    "https://www.reddit.com/r/TrueOffMyChest/"
]


def main():
    # PLEASE DO NOT UNCOMMENT AND RUN BEFORE SLEEP CALLS ARE ADDED TO AVOID IP BAN
    # for url in SUB_REDDIT_URLS:
    #     subreddit = SubReddit(url)
    #     subreddit.export()
    pass

if __name__ == "__main__":
    main()
