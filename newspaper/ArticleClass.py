'''
first commit from collaborator
'''
import codecs #This is for writing "strange"unicode chars like "thin space" into file 
import newspaper

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
        
def UploadArticle(newspaper_article):
    newspaper_article.download()
    newspaper_article.parse()
    a = ArticleClass()
    a.load_data(newspaper_article)
    return(a)
    
def UploadAll(html_page):
    newspaper_build_obj = newspaper.build(html_page, memoize_articles=False)
    s = newspaper_build_obj.size()
    article_list=[]    
    for i in range(s):
        art = newspaper_build_obj.articles[i]
        a = UploadArticle(art)
        article_list.append(a)
        print(str(i+1) + ' Title: ' + a.title.encode('ascii','ignore') + ' Text length: ' + str(len(a.text)))
    return(article_list)
    
        
