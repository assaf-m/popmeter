import codecs   # This is for writing "strange" unicode chars like "thin space" into file
import newspaper
import time
import DB_methods


MINIMUM_TEXT_LENGTH = 1000

class ArticleHandler(object):
    def __init__(self):
        self.url = ''   # a string containing the url of the article
        self.title = '' # a string containing the title of the article
        self.author_list = []   # a list containing the authors names (each one in a string)
        self.text = ''  # a string containing the body text of the article
        self.datetimestr = ''   # a string containing the date and time when article was added to list, in the form: YYYY MM DD HH MM SS
        self.valid = True   # a boolian indicating if this entry is a valid article
        self.validity_reason = 0    # an integer indicating if entry is a valid article
                                    # value meaning:
                                    # 0   - entry is valid
                                    # 100 - length of article text is shorter then MINIMUM_TEXT_LENGTH

    def load_data(self,article):
        self.url = article.url
        self.title = article.title
        self.author_list = article.authors
        self.text = article.text
        self.datetimestr = time.strftime('%Y %m %d %H %M %S')
        
    def write_to_file(self,fname):
        f = codecs.open(fname,'w',encoding='utf-8')
        f.write('URL:\n\r')
        f.write(self.url + '\n\r')
        f.write('Title:\n\r')
        f.write(self.title + '\n\r')
        auth_str=''
        for auth in self.author_list:
            auth_str = auth_str + ' ' + auth
        f.write('Authors:\n\r')
        f.write(auth_str + '\n\r')
        f.write('Text:\n\r')
        f.write(self.text + '\n\r')
        f.close()

    def check_validity(self):
        reason = 0
        if len(self.text) < MINIMUM_TEXT_LENGTH:
            reason = 100
        return reason


def UploadArticle(newspaper_article):
    newspaper_article.download()
    newspaper_article.parse()
    a = ArticleHandler()
    a.load_data(newspaper_article)

    return(a)


def UploadAll(html_page,collection):
    newspaper_build_obj = newspaper.build(html_page, memoize_articles=False)    # build a new newspapaer source
    s = newspaper_build_obj.size()
    article_list=[]
    j = 1
    # run on all articles in source and enter the articles into a list
    for i in range(s):
        art = newspaper_build_obj.articles[i]
        a = UploadArticle(art)
        validity_reason = a.check_validity()
        if validity_reason == 0:
            article_list.append(a)
            print(str(j) + ' Title: ' + a.title.encode('ascii','ignore') + '. Text length: ' + str(len(a.text)))
            j = j + 1
        else:
            print('Warning: article with title: ' + a.title.encode('ascii','ignore') + ', not valid, reason: ' + str(validity_reason))
            a.valid = False
            a.validity_reason = validity_reason
            article_list.append(a)
        #insert article, if it doesnt exist. notice the specification of the ID field and its corresponding value
        collection.insertArticle(articleObj= a,ID_field_name= 'title',ID_field_value = a.title)
    return(article_list)
