from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from .forms import LoginForm
from .views import RegisterView, profile

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'user/login.html', form_class = LoginForm, redirect_authenticated_user = True), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('sign_up/', RegisterView.as_view(), name='signup'),
    path('profile/', profile, name='profile')
]