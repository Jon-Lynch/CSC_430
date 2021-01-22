# Jonathan Lynch
# 5/9/20
# https://youtu.be/zDkN2he48-0
# "I have not given or received any unauthorized assistance on this assignment."

from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin
from re import findall


url = 'https://law.depaul.edu/Pages/default.aspx'

class Collector(HTMLParser):                                             # create subclass of superclass HTMLParser
    'class that parses information, returns links, returns data'
    def __init__(self, url):                                             # initialize class
        HTMLParser.__init__(self)                                        # extend HTMLParser __init__ overloaded operator
        self.url = url                                                   # initialize url input arg
        self.links = []                                                  # create empty list
        self.text = ''                                                   # create empty string
    def handle_starttag(self, tag, attrs):                               # overwrite method handle_starttag
        if tag == 'a':                                                   # determine if tag is 'a'
            for attr in attrs:                                           # iterate through attributes
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])                # transform href value to absolute url
                    if absolute[:22] == 'https://law.depaul.edu':        # only keep urls with a certain host name
                        self.links.append(absolute)                      # append to list self.links
    def getLinks(self):                                                  # create method getLinks
        return self.links                                                # return self.links list of links
    def handle_data(self, data):                                         # overwrite method handle_data
        self.text += data                                                # add data to self.txt string
    def getData(self):                                                   # create method getData
        return self.text                                                 # return data

def clean(content):
    'edits accepted string by locating patterns, then replacing items'
    pattern = '<p(.*?)</p>'                                # pattern to search for 
    words = findall(pattern, content)                      # locate pattern in string, assign it to words
    words = ''.join(words)                                 # transform words back into a string
    words = words.lower()                                  # make characters lower case
    words = words.replace('.', ' ')                        # replace all periods with empty string
    words = words.replace(',', ' ')                        # replace all commas with empty string
    words = words.replace('class=', ' ')                   # replace all 'class=' items with an empty string
    words = words.replace('<a', ' ')                       # replace all '<a' items with empty string
    words = words.replace('<u', ' ')                       # replace all '<u' items with empty string
    words = words.replace('</u', ' ')                      # replace all '</u' items with empty string
    words = words.replace('</a', ' ')                      # replace all '</a' items with empty string
    words = words.replace('<br/', ' ')                     # replace all '<br/' items with empty string
    words = words.replace('"', ' ')                        # replace all " with empty string
    words = words.replace('href', ' ')                     # replace all 'href' with empty string
    words = words.replace("'s", " ")                       # replace all "'s" with empty string
    words = words.replace('>', ' ')                        # replace all '>' with empty string
    words = words.replace('<span', ' ')                    # replace all '<span' with empty string
    words = words.replace("m30-b'", ' ')                   # replace all "m30-b'" with empty string
    words = words.replace("'https://law", ' ')             # replace all "'https://law" with empty string
    words = words.replace("aspx'", ' ')                    # replace all "aspx'" with empty string
    words = words.replace('/', ' ')                        # replace all '/' with empty string
    words = words.replace('(312)', ' ')                    # replace all '(312)' with empty string
    words = words.replace('<br', ' ')                      # replace all '<br' with empty string
    words = words.replace('<', ' ')                        # replace all '<' with empty string
    words = words.replace('edu', ' ')                      # replace all 'edu' with empty string
    words = words.replace('pages', ' ')                    # replace all 'pages' with empty sting
    words = words.replace('text-white', ' ')               # replace all 'text-white' with empty string
    words = words.replace("'m0-t", ' ')
    words = words.replace('=', ' ')
    words = words.replace('strong', ' ')
    return words
                                               
def analyze(url):
    'reads url into content, cleans and parses, locates and reads/cleans content of links, splits into list and uses dictionary as counter to return top 25 words'
    cleaned = ''                                                     # create empty string
    content = urlopen(url).read().decode()                           # open, read, and decode url, then set to content
    words = clean(content)                                           # clean content, and assign to words 
    cleaned += words                                                 # add words to empty string, cleaned
    collector = Collector(url)                                       # create instance object, collector, of Collector class
    collector.feed(content)                                          # feed content into collector
    links = collector.getLinks()                                     # get links of content using getLinks method from Collector class 
    linkslist = list(set(links))                                     # make use of set to eliminate duplicate links
    for link in linkslist:
        content = urlopen(link).read().decode()                      # open, read and decode each link, then set to content
        words = clean(content)                                       # clean content for each link, then set to words
        cleaned += words                                             # add words to string, cleaned
    cleaned = cleaned.split()                                        # split cleaned string into list of words
    dictionary = {}                                                  # create empty dictionary
    for word in cleaned:
        if word in dictionary:
            dictionary[word] += 1                                    # increment by one if word in dictionary
        else:
            dictionary[word] = 1                                                                           # set to 1, if word not in dictionary
    sorted_dict = sorted(dictionary, key=lambda x: (-dictionary[x], x))                                    # sort dictionary in decending order 
    print("The 25 most common words on DePaul's Law School website are: {}.".format(sorted_dict[0:25]))    # print values of first 25 dictionary items
    
    

