'''
'''
import ArticleHandler
from newspaper import Article
import random

TEST_DIR = 'E:\\Project\\Popmeter\\Test_Results\\'

def writeTestLog(text):
    print(text)

def writeTestResultToFile(fname, article):
    article.write_to_file(fname)

def runTest1(html_page, number_of_tests, news_paper_name):
    article_list = ArticleHandler.UploadAll(html_page)
    s = len(article_list)
    if (number_of_tests > s):
        n = 2
        writeTestLog('Number of tests greater then number of articles, n changed to 2')
    else:
        n = number_of_tests
    short_list = random.sample(article_list,n)
    i = 0
    for art in short_list:
        i = i + 1
        fname = TEST_DIR + news_paper_name + 'Test1_Result_' + str(i) + '.txt'
        art.write_to_file(fname)
        writeTestLog('Writing test result #' + str(i) +' to file: ' + fname)

def UnitTest():
# Washington Post Unit Test
    u='http://www.theguardian.com/commentisfree/2015/mar/20/prince-charles-america'
    #u ='http://www.washingtonpost.com/world/europe/a-month-after-kosher-market-attack-french-jews-plan-an-exodus/2015/02/07/bf7fd644-abb9-11e4-8876-460b1144cbc1_story.html?hpid=z1'
    article = Article(u)
    article.download()
    article.parse()
 
    a = ArticleHandler.ArticleHandler()
    a.load_data(article)
 
    fname = TEST_DIR + 'utest_wp.txt'
    a.write_to_file(fname)
