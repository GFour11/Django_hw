from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Author, Quotes
from django.core.paginator import Paginator
from .forms import NewAuthor, NewQuotes
def main(request, page =1):
    quotes = Quotes.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quote/index.html', context={'quotes':quotes_on_page})

def get_author(request, fullname):
    print(fullname)
    author = Author.objects.filter(fullname = fullname)[0]
    return render(request, 'quote/author.html', context={'author': author})

@login_required
def add_new_author(request):
    if request.method == 'POST':
        form = NewAuthor(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to = 'user:profile')
        else:
            return render(request, 'quote/add_author.html', context={'form': form})
    return render(request, 'quote/add_author.html', context={'form': NewAuthor})

@login_required
def add_new_quote(request):
    if request.method == 'POST':
        form = NewQuotes(request.POST)
        if form.is_valid():
            res = form.save(commit= False)
            res.tags = res.tags[0].split(' ')
            res.save()
            return redirect(to='user:profile')
        else:
            return render(request, 'quote/add_quotes.html', context={'form': form})
    return render(request, 'quote/add_quotes.html', context={'form': NewQuotes})