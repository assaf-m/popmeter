'''
first commit from collaborator
'''
import codecs #This is for writing "strange"unicode chars like "thin space" into file 
import newspaper
import DB_methods
import json

class ArticleClass(object):
#    def __init__(self):
#         p = newspaper.build(html_page, memoize_articles=False)
#         return(p)
                
    def load_data(self,article):
        self.url = article.url
        self.title = article.title
        self.author = article.authors
        self.text = article.text
        
    def write_to_file(self,fname):

        f = codecs.open(fname,'w',encoding='utf-8')
        f.write('URL:\n\r')
        f.write(self.url + '\n\r')
        f.write('Title:\n\r')
        f.write(self.title + '\n\r')
        f.write('Text:\n\r')
        f.write(self.text + '\n\r')
        f.close()
        
def UploadArticle(newspaper_article,collection):
    newspaper_article.download()
    newspaper_article.parse()
    a = ArticleClass()
    a.load_data(newspaper_article)
    #insert article, if it doesnt exist. notice the specification of the ID field and its corresponding value
    collection.insertArticle(articleObj= a,ID_field_name= 'title',ID_field_value = a.title)

    return(a)
    
def UploadAll(html_page,collection):
    newspaper_build_obj = newspaper.build(html_page, memoize_articles=False)
    s = newspaper_build_obj.size()
    article_list=[]    
    for i in range(s):
        art = newspaper_build_obj.articles[i]
        a = UploadArticle(art,collection)
        article_list.append(a)
        print(str(i+1) + ' Title: ' + a.title.encode('ascii','ignore') + ' Text length: ' + str(len(a.text)))
    return(article_list)
    
        
