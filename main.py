import time #importing the time library
import requests #importing the requests library
from bs4 import BeautifulSoup #importing the bs4 library
#get the start time
start = time.time()
#function that gets all links in the web page
def getLinks(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  links = []
  for link in soup.find_all('a'):
    links.append(link.get('href')) #finds all link with attr href
  return links
#now this is the real deal
weblink = 'https://en.wikipedia.org/wiki/World_War_II' #
links = getLinks(weblink) #remember the function we declared earlier
countLinks = 0 #this just count links
for link in links:
    link = str(link) #convert link to string Type
    countLinks += 1
    if len(str(link)) == 0:
      link = weblink
    if 'http://' in link:
      pass
    elif 'https://' in link:
      pass
    else:
      link = weblink+str(link)
    req = requests.get(link) #goes to the link
    if(req):
      print(link, req.status_code) #print the link and the response ie 200 for success or 404 if page not found
print('total no of links are '+str(countLinks))
end = time.time() #time at which it finished 
print('total time was '+str(round(end-start))+'s lolz :)')
