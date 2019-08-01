from article import Article
from source import Source
from urllib.request import urlopen
from bs4 import BeautifulSoup
import gzip

def main():
  print("News Mine")
  
#   s1 = Source("The News Minute", "tit", "aut", "201", "the")
#   print(s1)
  a1 = extractArticle("https://www.thenewsminute.com/article/rare-surgery-chennai-doctors-extract-526-teeth-7-year-olds-mouth-106448")
  print(a1)

  print(extractLinks("https://www.thenewsminute.com/section/Tamil%20Nadu"))
  


def extractLinks(ref):
  page = urlopen(ref)
  content = ""
  if page.info().get('Content-Encoding') == 'gzip':
      gzipFile = gzip.GzipFile(fileobj=page)
      content = gzipFile.read()
  else:
      content = page.read()
    
  soup = BeautifulSoup(content, "html.parser")
  
  links = []
  dirtyLinks = soup.find_all('h3')
  for dl in dirtyLinks:
      links.append(dl.find('a')['href'])
  return links
    


def extractArticle(ref):
  page = urlopen(ref)
  content = ""
  if page.info().get('Content-Encoding') == 'gzip':
      gzipFile = gzip.GzipFile(fileobj=page)
      content = gzipFile.read()
  else:
      content = page.read()
    
  soup = BeautifulSoup(content, "html.parser")

  title = soup.h1.get_text()
  
  published = soup.find('span', {'class': 'createddate'}).get_text().strip()

  paragraphs = soup.find('div', {'class': 'views-field-body'}).find_all('p')  
  content = ""
  for p in paragraphs:
      content = content + p.get_text() + "\n"

  return Article(title, "unable_to_extract", published, content, ref)


if __name__== "__main__":
  main()