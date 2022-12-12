from django.views.generic import DeleteView
from app.models import Televisores, Celulares, Notebooks
from django.urls import reverse_lazy


class DeleteTv(DeleteView):
    template_name = 'delete.html'
    model = Televisores
    fields = '__all__'
    success_url = reverse_lazy('show_tv')