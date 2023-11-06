import requests
import time

from bs4 import BeautifulSoup

POST_DIR = "./posts/"

class Post():
    def __init__(self, url: str, inHtml=False) -> None:
        if not url:
            self.title = ""
            self.post = ""
            self.fullText = ""
        else:
            # check if using HTML file for debugging
            # otherwise use requests to pull HTML from reddit
            self.fullText = open(url) if inHtml else (requests.get(url)).text
            
            soup = BeautifulSoup(self.fullText, 'html.parser')

            # find the title of the post
            
            titles = soup.find_all('shreddit-title')
            if len(titles) < 1:
                raise Exception()
            else:
                self.title = titles[0]['title'].split(":")[0].strip()
 

            # find the first item with the 'post' tag and create and array of all paragraphs in the post
            postChunks = soup.find_all('div', id=lambda x: x and 'post' in x)[0].find_all('p')

            pars = []
            for par in postChunks:
                pars.append(par.text)

            # join paragraphs with newline to create one large string for post
            self.post = '\n'.join(pars)
    
    # write each sentence to a text file separated by line delimiter
    def export(self):
        try:
            print(POST_DIR + self.title)
            f = open(POST_DIR + self.title, "w")
        except Exception:
            print("Unable to export: " + self.title)
            return

        for chunk in self.chunks:
            f.write(chunk)
            f.write("\n")
        f.close()
    
    # break larger post into individual sentences 
    def splitChunks(self):
        self.chunks = self.post.split(".")
        for i in range(len(self.chunks)):
            self.chunks[i] = self.chunks[i].strip().replace("\n", "")
    
    def condenseChunks(self):
        # create array for new chunks
        newChunks = [""]
        for chunk in self.chunks:
            # only add period if there is already a sentence there
            if (len(newChunks[-1]) > 0):
                newChunks[-1] += ". "
            
            # if sentences can be merged do so, otherwise start new sentence
            if len(newChunks[-1]) + len(chunk) + 2 <= 200:
                newChunks[-1] += chunk
            else:
                newChunks.append(chunk)
        
        self.chunks = newChunks
    
    # calls alls the functions needed to process and export post to text
    def process(self):
        self.splitChunks()
        self.condenseChunks()
        self.export()


class SubReddit:
    def __init__(self, url, inHtml=False) -> None:
        # if initilization is empty do nothing
        if not url:
            self.title = ""
            self.post = ""
            self.fullText = ""
        
        else:
            # check if using HTML file for debugging
            # otherwise use requests to pull HTML from reddit
            self.fullText = open(url) if inHtml else (requests.get(url)).text
            
            soup = BeautifulSoup(self.fullText, 'html.parser')
            
            # find all hyperlinks on the website
            self.all_links = soup.find_all('a')

            self.post_links = []

            for link in self.all_links:
                # if hyperlink leads to a post append it array of posts
                try:
                    if (link['slot'] == 'full-post-link'):
                        self.post_links.append(link['href'])
                except KeyError:
                    pass
            
            # create Post objects from links
            self.posts = []
            for l in self.post_links:
                time.sleep(1.5)
                try:
                    self.posts.append(Post("https://www.reddit.com" + l))
                
                except Exception:
                    print("Unable to generate post from " + l)
    
    # call export on all posts in the Subreddit object
    def export(self):
        for p in self.posts:
                p.process()

p = Post("aita.html", True)
p.process()