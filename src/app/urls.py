from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from app.views.home import Home
from app.views.create import CreateLaptop, CreatePhone, CreateTv
from app.views.show import mostrar_televisores, mostrar_celulares, mostrar_notebooks, mostrar_detalles
from app.views.about import about
from app.views.update import UpdateTv
from app.views.delete import DeleteTv


urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('create_phone/', CreatePhone.as_view(), name='create_phone'),
    path('create_tv/', CreateTv.as_view(), name ='create_tv'),
    path('create_laptop/', CreateLaptop.as_view(), name ='create_laptop'),
    path('mostrar_teles/', mostrar_televisores, name='show_tv'),
    path('mostrar_celulares/', mostrar_celulares, name='show_phone'),
    path('mostrar_notebooks/', mostrar_notebooks, name='show_laptop'),
    path('mostrar_producto/<str:categoria>/<int:id>',mostrar_detalles , name='details'),
    path('about_me/', about, name='aboutme'),
    path('update_tv/<pk>', UpdateTv.as_view(), name='updatetv_view'),
    path('delete_tv/<pk>', DeleteTv.as_view(), name='deletetv_view')
]



