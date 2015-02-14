import ArticleClass
import Test
import sys
wp_page = 'http://www.washingtonpost.com/'
wpArticleList = ArticleClass.UploadAll(wp_page)
print(len(wpArticleList))
Test.wpTest(wpArticleList[4])
