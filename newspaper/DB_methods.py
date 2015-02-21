__author__ = 'JohnGalt'
__author__ = 'JohnGalt'

import pymongo
import sys
import datetime

import json


class DB_worker:
    def __init__(self,port=None,host=None,dbName = None):
        self.dbName = dbName
        self.host = host
        self.port = port
        self.connection = self.mongo_connect()

    def mongo_connect(self):
        try:
            client = pymongo.MongoClient(port=self.port,host=self.host)
            db_con = client[self.dbName]
            return db_con
        except Exception as ex:
            print ex
            sys.exit()



class Collection_Ops:
    def __init__(self,collectionName = None,DB = None):
        self.collectionName = collectionName
        self.DB = DB
        self.collection = self.connect()

    def connect(self):
        return self.DB.connection[str(self.collectionName)]


    def insertArticle(self,articleObj= None,ID_field_name= None,ID_field_value=None):

        #TODO - Oded to determine article object structure and the ID field
        '''
        Insert the article into mongoDB
        :param articleObj: article object after Newspaper object transformation
        :param ID_field_name: The unique ID field of the article object which will determine if that article exists in the article or not
        :param ID_field_value:  The value of the ID field. We check if an articel with this name already exists in the DB

        :return:
        '''
        try:
            exists = self.lookForArticle(condition={ID_field_name:ID_field_value})
            if exists is not None:
                pass
            else:
                self.collection.insert(articleObj.__dict__)


        except Exception as ex:
            print ex
            sys.exit()

    def lookForArticle(self,condition):
        result = self.collection.find_one(condition)
        return result
