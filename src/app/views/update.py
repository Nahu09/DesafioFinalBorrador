from django.views.generic import UpdateView
from app.models import Televisores, Celulares, Notebooks
from django.urls import reverse_lazy


class UpdateTv(UpdateView):
    template_name = 'update.html'
    model = Televisores
    fields = '__all__'
    success_url = reverse_lazy('show_tv')

class UpdatePhone(UpdateView):
    template_name = 'update.html'
    model = Celulares
    fields = '__all__'
    success_url = reverse_lazy('show_phone')
    
class UpdatePhone(UpdateView):
    template_name = 'update.html'
    model = Notebooks
    fields = '__all__'
    success_url = reverse_lazy('show_laptop')