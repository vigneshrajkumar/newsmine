class Source:
  def __init__(self, name, titlePtr, authorPrt, publishedPtr, contentPrt):
    self.name = name
    self.titlePtr = titlePtr
    self.authorPrt = authorPrt
    self.publishedPtr = publishedPtr
    self.contentPrt = contentPrt

  def __str__(self):
      return "{ src: " + self.name + " }"