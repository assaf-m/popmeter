import ArticleClass
import Test
import DB_methods
import sys

db = DB_methods.DB_worker(dbName = 'newDB',port=27017,host='localhost') #mongo DB conenction initialized
collection  = DB_methods.Collection_Ops(collectionName='articles',DB=db) #specify the colelction to work on
wp_page = 'http://www.cnn.com/'
wpArticleList = ArticleClass.UploadAll(wp_page,collection)
print(len(wpArticleList))
Test.wpTest(wpArticleList[4])
