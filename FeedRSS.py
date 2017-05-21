import feedparser
import json
from array import array

def feedReader():
    linkList = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
                'https://atwar.blogs.nytimes.com/feed/',
                'http://rss.nytimes.com/services/xml/rss/nyt/Americas.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/US.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Education.xml',
                'https://learning.blogs.nytimes.com/feed/',
                'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Upshot.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml',
                'https://cityroom.blogs.nytimes.com/feed/',
                'http://rss.nytimes.com/services/xml/rss/nyt/Business.xml
                'http://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Economy.xml',
                'http://www.nytimes.com/services/xml/rss/nyt/Dealbook.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/YourMoney.xml',
                'http://feeds.foxnews.com/foxnews/latest',
                'http://feeds.foxnews.com/foxnews/politics',
                'http://feeds.foxnews.com/foxnews/health',
                'http://feeds.foxnews.com/foxnews/section/lifestyle',
                'http://feeds.foxnews.com/foxnews/opinion',
                'http://feeds.foxnews.com/foxnews/most-popular',
                'http://feeds.foxnews.com/foxnews/science',
                'http://feeds.foxnews.com/foxnews/tech',
                'http://feeds.foxnews.com/foxnews/internal/travel/mixed',
                'http://feeds.foxnews.com/foxnews/national',
                'http://feeds.foxnews.com/foxnews/video',
                'http://feeds.foxnews.com/foxnews/world',
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
