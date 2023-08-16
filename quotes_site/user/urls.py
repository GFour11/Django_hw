from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView

from .forms import LoginForm
from .views import RegisterView, profile, ResetPasswordView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'user/login.html', form_class = LoginForm, redirect_authenticated_user = True), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('sign_up/', RegisterView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('reset-password/', ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',
                                          success_url='user/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
]