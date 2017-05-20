def feedReader():
    linkList = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://www.reuters.com/tools/rss',
                'http://www.foxnews.com/about/rss/',
                'http://www.upi.com/rss/',
                'https://www.usatoday.com/rss/',
                'https://wildfires.einnews.com/all_rss',
                'http://www.cnn.com/services/rss/',
                'https://www.lib.noaa.gov/rss.html',
                'http://www.aviationsafetymagazine.com/rss/']
    for link in linkList:
        parsedLink = feedparser.parse(link)
        return parsedLink['entries']
