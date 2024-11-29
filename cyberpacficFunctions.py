import requests
from bs4 import BeautifulSoup

class Extraction:
  def __init__(self, header):
    self.header = header

  def parse_data(self, link):
    #Get the data from a specific site. Returns the sorted data with [weblink, title] format.
    #-----
    webpage = requests.get(link, headers = self.header)

    # Init BeautifulSoup and parse the webpage
    bs = BeautifulSoup(webpage.content, "html.parser")

    #Collects all of the attributes with links. Order is in [weblink, attribute text]
    filteredData = bs.find_all('a', href = True)
    extractedData = []

    for i in filteredData:
      if i.text:
        temp = [i['href'], i.text]
        extractedData.append(temp)
    
    return (extractedData)

  def find_value(self, parsedData, value, listIndex = 0):
    #Finds and returns index where value can be found in parsedData. Must be a 2d array, can specify which index of the sublist you want to check.
    indexFound = [i for i in range(len(parsedData)-1) if str(value) == parsedData[i][listIndex]][0]

    return indexFound
  
  def filter_data(self, parsedData, startIndex = 0, endIndex = -1):
    #Filters data from the startIndex + 1 to endIndex. Default will be start to end.
    return parsedData[(startIndex) : (endIndex)]

  def check_correct(self, filteredData, filterIndex, targetIndex):
    #Print (Bool, filteredData[filterIndex], filteredData[targetIndex]).
    checkTrue = filteredData[filterIndex] == filteredData[targetIndex]

    print(checkTrue, filteredData[filterIndex], filteredData[targetIndex])
    return()

    

