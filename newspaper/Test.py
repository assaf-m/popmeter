'''
'''
import ArticleClass
from newspaper import Article

def wpTest(a):
# Washington Post test
    fname = 'test_wp.txt'
    a.write_to_file(fname)

def wpUnitTest(a):
# Washington Post Unit Test
    u ='http://www.washingtonpost.com/world/europe/a-month-after-kosher-market-attack-french-jews-plan-an-exodus/2015/02/07/bf7fd644-abb9-11e4-8876-460b1144cbc1_story.html?hpid=z1'
    article = Article(u)
    article.download()
    article.parse()
 
    a = ArticleClass.ArticleClass()
    a.load_data(article)
 
    fname = 'utest_wp.txt'
    a.write_to_file(fname)
