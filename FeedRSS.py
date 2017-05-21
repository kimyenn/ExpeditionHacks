import feedparser
import json
from array import array

def feedReader():
    linkList = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                'http://rss.cnn.com/rss/cnn_topstories.rss',
                'http://rss.cnn.com/rss/cnn_health.rss',
                'http://rss.cnn.com/rss/cnn_showbiz.rss',
                'http://rss.cnn.com/rss/cnn_travel.rss',
                'http://rss.cnn.com/rss/cnn_living.rss',
                'http://rss.cnn.com/services/podcasting/cnn10/rss.xml',
                'http://rss.cnn.com/rss/cnn_latest.rss',
                'http://rss.cnn.com/rss/money_markets.rss'
                'http://rss.cnn.com/rss/cnn_health.rss',
                'http://rss.cnn.com/rss/cnn_world.rss',
                'http://rss.cnn.com/rss/cnn_us.rss',
                'http://rss.cnn.com/rss/money_latest.rss',
                'http://rss.cnn.com/rss/cnn_allpolitics.rss',
                'http://rss.cnn.com/rss/cnn_tech.rss',
                'http://rss.cnn.com/rss/money_technology.rss',
                'http://rss.cnn.com/rss/cnn_topstories.rss',
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
    
    feeds = []
    for link in linkList:
        parsedLink = feedparser.parse(link)
        
        for entry in parsedLink.entries:
            feedEntry = [entry['title'], entry['title_detail']['value'], 
                     entry['summary'],
                     entry['summary_detail']['value'], 
                     entry['link']]
            feeds.append(feedEntry)
    return feeds
