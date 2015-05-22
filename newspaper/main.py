import Test

url_list=[r'http://www.theguardian.com/uk',\
          r'http://www.theguardian.com/world',\
          r'http://www.theguardian.com/world/europe-news',\
          r'http://www.theguardian.com/us-news',\
          r'http://www.theguardian.com/world/americas',\
          r'http://www.theguardian.com/australia-news',\
          r'http://www.theguardian.com/world/africa',\
          r'http://www.theguardian.com/world/middleeast',\
          r'http://www.theguardian.com/cities',\
          r'http://www.theguardian.com/global-development',\
          r'http://www.theguardian.com/politics',\
          r'http://www.theguardian.com/uk/commentisfree',\
          r'http://www.theguardian.com/index/contributors',\
          r'http://www.theguardian.com/uk/culture',\
          r'http://www.theguardian.com/uk/business',\
          r'http://www.theguardian.com/business/economics',\
          r'http://www.theguardian.com/business/banking',\
          r'http://www.theguardian.com/business/retail',\
          r'http://www.theguardian.com/business/eurozone',\
          r'http://www.theguardian.com/lifeandstyle',\
          r'http://www.theguardian.com/fashion',\
          r'http://www.theguardian.com/uk/environment',\
          r'http://www.theguardian.com/uk/technology',\
          r'http://www.theguardian.com/travel']

for url in url_list:
    Test.runTest1(url)
# x = MostPopularHandler.ArticlesFromMostPopularList('The Guardian')
# y=x.article_list[0]
# print y.address
# print y.category
# print len(x.article_list)
# print x.datetimestr
