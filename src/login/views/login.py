from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.


class Login(LoginView):
    template_name = 'login.html'
    #success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class AdminLogoutView(LogoutView):
    #template_name = 'login.html'
    next_page = 'login_view'


