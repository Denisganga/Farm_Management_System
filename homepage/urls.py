from django.urls import path
from .views import (Mainpage,Show_employees,Add_employees)

app_name='homepage'

urlpatterns =[
    path('mainpage/', Mainpage, name='mainpage'),
    path('show_employees/', Show_employees, name='show-employees'),
    path('add_employees/', Add_employees, name='add-employees'),
]