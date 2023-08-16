from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from .forms import RegisterForm

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'user/password_reset.html'
    email_template_name = 'user/password_reset_email.html'
    html_email_template_name = 'user/password_reset_email.html'
    success_url = reverse_lazy('user:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'user/password_reset_subject.txt'
class RegisterView(View):
    template_name = 'user/sign_up.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to= 'user:login')
        return render(request, self.template_name, {'form': form})

def profile(request):
    return render(request, 'user/profile.html')