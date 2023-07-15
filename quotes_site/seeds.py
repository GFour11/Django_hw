from pymongo import MongoClient
import certifi


ca = certifi.where()

client = MongoClient("mongodb+srv://ulchegor1:ujhsysx1@cluster0.m5zgbn0.mongodb.net/FCollection?retryWrites=true&w=majority", tlsCAFile=ca)

db = client['FCollection']


def get_authors():
    collection = db['author']
    result = collection.find()
    return result

def get_qoutes():
    collection = db['quotes']
    result = collection.find()
    return result
if __name__ == '__main__':
    print('Hello')

