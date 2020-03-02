__author__ = "JrReubinJr"

import pymongo
import dns

class Database(object):
    path = "C:\Program Files\MongoDB\Server\MongoLogin.txt"
    file = open(path, 'r')
    uri = file.read()
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['blogDB']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query): #returns pymongo cursor object
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query): #return first element return from cursor (json object)
        return Database.DATABASE[collection].find_one(query)