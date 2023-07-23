import certifi
import os
import django
from pymongo import MongoClient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'quotes_site.settings')
django.setup()

from quote.models import Author, Quotes


ca = certifi.where()

client = MongoClient("mongodb+srv://ulchegor1:ujhsysx1@cluster0.m5zgbn0.mongodb.net/Django?retryWrites=true&w=majority", tlsCAFile=ca)

db = client['Django']


def get_authors():
    collection = db['author']
    result = collection.find({})
    for el in result:
        Author(fullname = el['fullname'], born_date= el['born_date'], born_location = el['born_location'], description = el['description']).save()


def get_qoutes():
    result = db.quotes.find()
    for quote in result:
        print(quote['author'])
        author = db.author.find_one({'_id': quote['author']})
        print(author)
        author_el = Author.objects.filter(born_date = author['born_date'])
        print(type(author_el))
        Quotes(tags = quote['tags'], author = author_el[0], quotes =quote['quotes']).save()

if __name__ == '__main__':
    get_authors()
    get_qoutes()
