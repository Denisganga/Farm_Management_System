from django.urls import path
from .views import (
    Mainpage,
    Show_employees,
    Add_employees,
    Delete_employees,
    Update_employees,
    Show_crops,
    Add_crops,
    Update_crops,
    Delete_crops,
    Show_machinery,
    Add_machinery,
    Delete_machinery,
    Update_machinery,
    Show_livestock,
    Add_livestock,
    Update_livestock,
    Delete_livestock,
    Show_livestock_production,
    Add_livestock_production,
    Delete_livestock_production,
    Update_livestock_production
    
)

app_name = "homepage"

urlpatterns = [
    path("", Mainpage, name="mainpage"),
    path("show_employees/", Show_employees, name="show-employees"),
    path("add_employees/", Add_employees, name="add-employees"),
    path("delete_employees/<int:Eid>/", Delete_employees, name="delete-employees"),
    path("update_employees/<int:Eid>/", Update_employees, name="update-employees"),
    path("show_crops/", Show_crops, name="show-crops"),
    path("add-crops/", Add_crops, name="add-crops"),
    path("update_crops/<int:Cid>/", Update_crops, name="update-crops"),
    path("delete_crops/<int:Cid>/", Delete_crops, name="delete-crops"),
    path('show_machinery/', Show_machinery, name="show-machinery"),
    path("add-machinery/", Add_machinery, name="add-machinery"),
    path("delete_machinery/<str:Number_plate>/", Delete_machinery, name="delete-machinery",),
    path("update_machinery/<str:Number_plate>/", Update_machinery, name="update-machinery"),
    path("show_livestock/", Show_livestock, name="show-livestock"),
    path("add_livestock/", Add_livestock,name="add-livestock"),
    path("update_livestock/<str:Tag_number>/", Update_livestock, name="update-livestock" ),
    path("delete_livestock/<str:Tag_number>/", Delete_livestock, name="delete-livestock"),
    path('show_livestockproduction/<str:Tag_number>/', Show_livestock_production, name='show-livestockproduction'),
    path('add_livestockproduction/<str:Tag_number>/',Add_livestock_production, name='add-livestockproduction'),
    path('delete_livestockproduction/<str:Tag_number>/<slug:Production_date>/', Delete_livestock_production, name='delete-livestockproduction'),
    path('update_levestockproduction/<str:Tag_number>/<slug:Production_date>/', Update_livestock_production, name='update-livestockproduction'),
]
