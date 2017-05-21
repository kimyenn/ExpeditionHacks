import feedparser
import json
from array import array

def feedReader():
    linkList = ['http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
                'https://atwar.blogs.nytimes.com/feed/',
                'http://rss.nytimes.com/services/xml/rss/nyt/Americas.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/US.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Education.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Upshot.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml',
                'https://cityroom.blogs.nytimes.com/feed/',
                'http://rss.nytimes.com/services/xml/rss/nyt/Business.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Economy.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Science.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/Research.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/HealthCarePolicy.xml',
                'http://rss.nytimes.com/services/xml/rss/nyt/MostViewed.xml',
                'http://topics.nytimes.com/top/opinion/editorialsandoped/editorials/index.html?rss=1',
                'http://topics.nytimes.com/top/opinion/editorialsandoped/oped/contributors/index.html?rss=1',
                'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
                'http://hosted2.ap.org/atom/APDEFAULT/386c25518f464186bf7a2ac026580ce7',
                'http://hosted2.ap.org/atom/APDEFAULT/386c25518f464186bf7a2ac026580ce7',
                'http://hosted2.ap.org/atom/APDEFAULT/89ae8247abe8493fae24405546e9a1aa',
                'http://hosted2.ap.org/atom/APDEFAULT/f70471f764144b2fab526d39972d37b3',
                'http://hosted2.ap.org/atom/APDEFAULT/495d344a0d10421e9baa8ee77029cfbd',
                'http://hosted2.ap.org/atom/APDEFAULT/347875155d53465d95cec892aeb06419',
                'http://hosted2.ap.org/atom/APDEFAULT/4e67281c3f754d0696fbfdee0f3f1469',
                'http://hosted2.ap.org/atom/APDEFAULT/bbd825583c8542898e6fa7d440b9febc',
                'http://hosted2.ap.org/atom/APDEFAULT/b2f0ca3a594644ee9e50a8ec4ce2d6de',
                'http://hosted2.ap.org/atom/APDEFAULT/aa9398e6757a46fa93ed5dea7bd3729e',
                'http://feeds.foxnews.com/foxnews/latest',
                'http://feeds.foxnews.com/foxnews/politics',
                'http://feeds.foxnews.com/foxnews/health',
                'http://feeds.foxnews.com/foxnews/most-popular',
                'http://feeds.foxnews.com/foxnews/science',
                'http://feeds.foxnews.com/foxnews/tech',
                'http://feeds.foxnews.com/foxnews/national',
                'http://feeds.foxnews.com/foxnews/world',
                'http://rss.cnn.com/rss/cnn_topstories.rss',
                'http://rss.cnn.com/rss/cnn_latest.rss',
                'http://rss.cnn.com/rss/money_markets.rss'
                'http://rss.cnn.com/rss/cnn_world.rss',
                'http://rss.cnn.com/rss/cnn_us.rss',
                'http://rss.cnn.com/rss/money_latest.rss',
                'http://rss.cnn.com/rss/cnn_allpolitics.rss',
                'http://rss.cnn.com/rss/cnn_tech.rss',
                'http://rss.cnn.com/rss/money_technology.rss',
                'http://rss.cnn.com/rss/cnn_topstories.rss',
                'http://feeds.reuters.com/reuters/businessNews',
                'http://feeds.reuters.com/reuters/MostRead',
                'http://feeds.reuters.com/Reuters/PoliticsNews',
                'http://feeds.reuters.com/reuters/scienceNews',
                'http://feeds.reuters.com/reuters/technologyNews',
                'http://feeds.reuters.com/reuters/topNews',
                'http://feeds.reuters.com/Reuters/domesticNews',
                'http://feeds.reuters.com/Reuters/worldNews']
    
    feeds = []
    for link in linkList:

        parsedLink = feedparser.parse(link)
        
        for entry in parsedLink.entries:
            feedEntry = [entry['title'], 
                     entry['summary'], 
                     entry['link']]
            if entry['summary'].startswith("<") == False:
                feeds.append(feedEntry)
    return feeds

