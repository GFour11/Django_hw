from django.contrib.postgres.fields import ArrayField
from django.forms import ModelForm, CharField, TextInput, ModelChoiceField
from .models import Author, Quotes

class NewAuthor(ModelForm):
    fullname = CharField(max_length=100, required=True, widget=TextInput(attrs={"class": "form-control"}))
    born_date = CharField(required=True, widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(required=True, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(required=True, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ('fullname','born_date', 'born_location', 'description')


class NewQuotes(ModelForm):
    tags = ArrayField((CharField(required=True, widget=TextInput(attrs={"class": "form-control"}))))
    author = ModelChoiceField(queryset=Author.objects.all().values_list('fullname', flat=True).order_by('fullname'))
    quotes = CharField()

    class Meta:
        model = Quotes
        fields = ('tags', 'author', 'quotes')

