from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from app.models import Televisores, Notebooks, Celulares
from app.form import CreateTv, CreateLaptop, CreatePhone




class CreateTv(CreateView):
    template_name = 'create.html'
    form_class = CreateTv
    success_url = reverse_lazy('home')
    model = Televisores
    #fields = '__all__'

class CreatePhone(CreateView):
    template_name = 'create.html'
    form_class = CreatePhone
    success_url = reverse_lazy('home')
    model = Celulares


class CreateLaptop(CreateView):
    template_name = 'create.html'
    form_class = CreateLaptop
    success_url = reverse_lazy('home')
    model = Notebooks





    
