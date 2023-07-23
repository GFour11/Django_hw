from django.shortcuts import render, redirect
from django.views import View

from .forms import RegisterForm

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