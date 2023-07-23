from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_author', views.add_new_author, name='new-author'),
    path('add_quotes', views.add_new_quote, name='new-quotes'),
    path('<int:page>', views.main, name='paginate'),
    path('<str:fullname>', views.get_author, name='author-detail'),

]