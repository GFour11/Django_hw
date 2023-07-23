from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, ForeignKey
from django.contrib.postgres.fields import ArrayField



class Author(models.Model):
    fullname = CharField(max_length=100, unique= True)
    born_date = CharField()
    born_location = CharField()
    description = CharField()


class Quotes(models.Model):
    tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    author = ForeignKey(Author, on_delete=models.CASCADE)
    quotes = CharField()



