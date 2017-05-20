import feedparser
import json
def feedReader():
    linkList = ['http://www.reuters.com/tools/rss',
                'http://feeds.bbci.co.uk/news/world/rss.xml',
                'http://feeds.reuters.com/news/artsculture',
                'http://feeds.reuters.com/reuters/businessNews',
                'http://feeds.reuters.com/reuters/companyNews',
                'http://rss.cnn.com/rss/cnn_topstories.rss',
                'http://feeds.reuters.com/reuters/environment',
                'http://feeds.reuters.com/reuters/healthNews',
                'http://feeds.reuters.com/reuters/lifestyle',
                'http://feeds.reuters.com/news/wealth',
                'http://feeds.reuters.com/reuters/MostRead',
                'http://feeds.reuters.com/reuters/oddlyEnoughNews',
                'http://feeds.reuters.com/ReutersPictures',
                'http://feeds.reuters.com/reuters/peopleNews',
                'http://feeds.reuters.com/Reuters/PoliticsNews',
                'http://feeds.reuters.com/reuters/scienceNews',
                'http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml?edition=int',
                'http://feeds.reuters.com/reuters/technologyNews',
                'http://feeds.reuters.com/reuters/topNews',
                'http://feeds.reuters.com/Reuters/domesticNews',
                'http://feeds.reuters.com/Reuters/worldNews',
                'http://www.aviationsafetymagazine.com/rss/']
    feeds = []
    for link in linkList:
        parsedLink = feedparser.parse(link)
        
        for entry in parsedLink.entries:
            feedEntry = [entry['title'], entry['title_detail']['value'], 
                     entry['summary'],
                     entry['summary_detail']['value'], 
                     entry['link'],
                     entry['published'],
                     entry['published_parsed']]
            feeds.append(feedEntry)
