class Article:
  def __init__(self, title, author, published, content, reference):
    self.title = title
    self.author = author
    self.published = published
    self.content = content
    self.reference = reference

  def __str__(self):
      return "{ TITLE: " + self.title[:20] + ".. ; CONTENT: " + self.content[:30] +".. ; BY: " + self.author  +  "; DATE: "+ self.published + "}"