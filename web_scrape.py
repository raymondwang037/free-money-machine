import requests

from bs4 import BeautifulSoup

class Post():
    def __init__(self, url: str, inHtml=False) -> None:
        if not url:
            self.title = ""
            self.post = ""
            self.fullText = ""
        else:
            self.fullText = open(url) if inHtml else (requests.get(url)).text
            
            soup = BeautifulSoup(self.fullText, 'html.parser')

            self.title = soup.find_all('shreddit-title')[0]['title'].split(":")[0].strip()

            postChunks = soup.find_all('div', id=lambda x: x and 'post' in x)[0].find_all('p')

            pars = []
            for par in postChunks:
                pars.append(par.text)

            self.post = '\n'.join(pars)
    
    def exportToText(self):
        f = open(self.title, "w")
        for chunk in self.chunks:
            f.write(chunk)
            f.write("\n----------\n")
        # f.write(self.post)
        f.close()
    
    def splitChunks(self):
        self.chunks = self.post.split(".")
        for i in range(len(self.chunks)):
            self.chunks[i] = self.chunks[i].strip().replace("\n", "")

class SubReddit:
    def __init__(self, url, inHtml=False) -> None:
        if not url:
            self.title = ""
            self.post = ""
            self.fullText = ""
        
        else:
            self.fullText = open(url) if inHtml else (requests.get(url)).text
            
            soup = BeautifulSoup(self.fullText, 'html.parser')
            

            self.all_links = soup.find_all('a')

            self.post_links = []

            for link in self.all_links:
                try:
                    if (link['slot'] == 'full-post-link'):
                        self.post_links.append(link['href'])
                except KeyError:
                    pass
            
            self.posts = []
            for l in self.post_links:
                self.posts.append(Post(l))
            
            for p in self.posts:
                p.splitChunks()
                p.exportToText()
                    
        
r = SubReddit("Am I the Asshole .html", True)    

# p = Post("aita.html", True)
# p.splitChunks()
# p.exportToText()
