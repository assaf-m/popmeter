from bs4 import BeautifulSoup
import requests
import time


THE_GUARDIAN_MOST_POPULAR_HTML_PAGE = "http://www.theguardian.com/most-read"
THE_GUARDIAN_CSS_SELECTOR = "div.fc-item__content a[href]"
THE_GUARDIAN_PUBLICATION_ID = "The Guardian"

class ArticleDescription(object):
    def __init__(self):
        self.category = ''
        self.address = ''

class ArticlesFromMostPopularList(object):
    def __init__(self,publication):
        self.publication = publication # a string containing the publication name of the article
        self.article_list=self.get()    # a list containing tuples, each one with:
                                        #   article address - a string containing article's url
                                        #   article category - a string containing article's category
        self.datetimestr = time.strftime('%Y %m %d %H %M %S') # a string containing the date and time when article was added to list, in the form: YYYY MM DD HH MM SS

    def get(self):
        if self.publication == THE_GUARDIAN_PUBLICATION_ID:
            return(self.get_FromTheGuardian(THE_GUARDIAN_MOST_POPULAR_HTML_PAGE))

    def get_FromTheGuardian(self,html_address):
        page = requests.get(html_address)
        bs_obj = BeautifulSoup(page.text,'html5lib')
        all_selector_list = bs_obj.body.select(THE_GUARDIAN_CSS_SELECTOR)
        all_url_list = []
        for selector in all_selector_list:
            art = ArticleDescription()
            art.address = selector.get('href')
            temp_str = art.address.split('/')
            art.category = temp_str[3]
            all_url_list.append(art)
        return(all_url_list)
