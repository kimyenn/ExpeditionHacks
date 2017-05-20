import feedparser
import json
def feedReader():
    linkList = ['http://www.reuters.com/tools/rss',
                'http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://feeds.reuters.com/news/artsculture',
                'http://feeds.reuters.com/reuters/businessNews',
                'http://feeds.reuters.com/reuters/companyNews',
                'http://feeds.reuters.com/reuters/entertainment',
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
                'http://feeds.reuters.com/reuters/sportsNews',
                'http://feeds.reuters.com/reuters/technologyNews',
                'http://feeds.reuters.com/reuters/topNews',
                'http://feeds.reuters.com/Reuters/domesticNews',
                'http://feeds.reuters.com/Reuters/worldNews',
                'http://www.aviationsafetymagazine.com/rss/']
    for link in linkList:
        print(link)
        parsedLink = feedparser.parse(link)
        print(parsedLink)
