from article import Article
from source import Source
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
  print("News Mine")
  a1 = Article("tit", "aut", "201", "the", "www")
  print(a1)

  s1 = Source("The News Minute", "tit", "aut", "201", "the")
  print(s1)

  page = urlopen("https://www.thenewsminute.com/article/rare-surgery-chennai-doctors-extract-526-teeth-7-year-olds-mouth-106448").read()
  
  print(page)

  
  
#   print(page.read()

#   soup = BeautifulSoup(page, "html.parser")

#   print(soup)





if __name__== "__main__":
  main()