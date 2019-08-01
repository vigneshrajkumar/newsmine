from article import Article
from source import Source
from urllib.request import urlopen
from bs4 import BeautifulSoup
import gzip

def main():
  print("News Mine")
  a1 = Article("tit", "aut", "201", "the", "www")
  print(a1)

  s1 = Source("The News Minute", "tit", "aut", "201", "the")
  print(s1)

  page = urlopen("https://www.thenewsminute.com/article/rare-surgery-chennai-doctors-extract-526-teeth-7-year-olds-mouth-106448")

  content = ""

  if page.info().get('Content-Encoding') == 'gzip':
      print("gzip comp")

      gzipFile = gzip.GzipFile(fileobj=page)
      content = gzipFile.read()
  else:
      print("nah")
      content = page.read()


  


  soup = BeautifulSoup(content, "html.parser")

  print(soup.h1)





if __name__== "__main__":
  main()