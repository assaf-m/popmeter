'''
'''
import ArticleHandler
import newspaper
import DB_methods
import MostPopularHandler


TEST_DIR = 'E:\\Project\\Popmeter\\Test_Results\\'

def writeTestLog(text):
    print(text)

def writeTestResultToFile(fname, article):
    article.write_to_file(fname)

def runTest1(html_page):
    #html_page = 'http://www.theguardian.com/politics'

    db = DB_methods.DB_worker(dbName = 'newDB',port=27017,host='localhost') #mongo DB connection initialized
    collection  = DB_methods.Collection_Ops(collectionName='articles',DB=db) #specify the collection to work on
    article_list = ArticleHandler.UploadAll(html_page,collection)
    # article_list = ['1', '2']
    grd_mostpop = MostPopularHandler.ArticlesFromMostPopularList('The Guardian')
    list_len = len(grd_mostpop.article_list)
    writeTestLog('The most popular articles list has: ' + str(list_len) + ' articles')
    num_of_hits = 0
    i=0
    for i in range(0, list_len-1):
        url = grd_mostpop.article_list[i].address
        j = 0
        for j in range (0,len(article_list)-1):
            if (article_list[j].url == url):
                num_of_hits += 1
                writeTestLog('found article #' + str(i) + ' (' + url + ')' )
                break
                # j = len(article_list)-1
            else:
                if (j == len(article_list)-1):
                    writeTestLog('did not find article #' + str(i) + ' (' + url + ')' )
    writeTestLog('found ' + str(num_of_hits) + ' out of ' + str(list_len) + ' articles')



def UnitTest():
# Washington Post Unit Test
    u='http://www.theguardian.com/commentisfree/2015/mar/20/prince-charles-america'
    #u ='http://www.washingtonpost.com/world/europe/a-month-after-kosher-market-attack-french-jews-plan-an-exodus/2015/02/07/bf7fd644-abb9-11e4-8876-460b1144cbc1_story.html?hpid=z1'
    article = newspaper.Article(u)
    article.download()
    article.parse()
 
    a = ArticleHandler.ArticleHandler()
    a.load_data(article)
 
    fname = TEST_DIR + 'utest_wp.txt'
    a.write_to_file(fname)
