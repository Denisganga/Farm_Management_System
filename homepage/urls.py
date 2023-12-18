from django.urls import path
from .views import (Mainpage,Show_employees,Add_employees,Delete_employees,Update_employees,Show_crops,Add_crops,Update_crops)

app_name='homepage'

urlpatterns =[
    path('mainpage/', Mainpage, name='mainpage'),
    path('show_employees/', Show_employees, name='show-employees'),
    path('add_employees/', Add_employees, name='add-employees'),
    path('delete_employees/<int:Eid>/', Delete_employees, name='delete-employees'),
    path('update_employees/<int:Eid>/', Update_employees, name='update-employees'),
    path('show_crops/', Show_crops, name='show-crops'),
    path('add-crops/', Add_crops, name= 'add-crops'),
    path('update_crops/<int:Cid>/', Update_crops, name='update-crops'),
]