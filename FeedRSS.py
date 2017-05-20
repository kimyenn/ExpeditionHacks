def feedReader():
    linkList = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
                'http://www.reuters.com/tools/rss',
               'http://www.foxnews.com/about/rss/']
    for link in linkList:
        parsedLink = feedparser.parse(link)
        return parsedLink['entries']
