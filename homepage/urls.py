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
    Update_livestock_production,
    Show_crop_expenses,
    Add_crop_expenses,
    Update_crop_expenses,
    Delete_crop_expenses,
    Show_crop_sales,
    Add_crop_sales,
    Delete_crop_sales,
    Update_crop_sales,
    Show_crop_operations,
    Add_crop_operations,
    Delete_crop_operations,
    Update_crop_operations,
    Show_machinery_activities,
    Add_machinery_activities,
    Delete_machinery_activity,
    Update_machinery_activities,
    Show_machinery_maintenance
    
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

    path('update_livestockproduction/<str:Tag_number>/<slug:Production_date>/', Update_livestock_production, name='update-livestockproduction'),

    path('show_cropexpenses/<int:Cid>/', Show_crop_expenses, name='show-cropexpenses'),

    path('add_cropexpenses/<int:Cid>/', Add_crop_expenses, name="add-cropexpenses"),

    path('update_cropexpense/<int:Cid>/<slug:Expense_date>/', Update_crop_expenses, name='update-cropexpenses'),

    path('delete_cropexpenses/<int:Cid>/<slug:Expense_date>/', Delete_crop_expenses, name='delete-cropexpenses'),

    path('show_cropsales/<int:Cid>/', Show_crop_sales, name="show-cropsales"),

    path('add_cropsales/<int:Cid>/', Add_crop_sales, name='add-cropsales'),

    path('delete_cropsales/<int:Cid>/<slug:Sale_date>/', Delete_crop_sales, name='delete-cropsales'),

    path('update_cropsales/<int:Cid>/<slug:Sale_date>/', Update_crop_sales, name='update-cropsales'),

    path('show_cropoperations/<int:Cid>/', Show_crop_operations, name='show-cropoperations'),

    path('add_cropoperations/<int:Cid>/', Add_crop_operations, name='add-cropoperations'),

    path('delete_cropoperations/<int:Cid>/<slug:Operation_date>/', Delete_crop_operations, name='delete-cropoperations'),

    path('update_cropoperations/<int:Cid>/<slug:Operation_date>/', Update_crop_operations, name='update-cropoperations'),

    path('show_machineryactivities/<str:Number_plate>/', Show_machinery_activities, name='show-machineryactivities'),

    path('add_machineryactivirties/<str:Number_plate>/', Add_machinery_activities, name="add-machineryactivities"),

    path('delete_machineryactivities/<str:Number_plate>/<slug:Activity_date>/', Delete_machinery_activity, name='delete-machineryactivities'),

    path('update_machineryactivities/<str:Number_plate>/<slug:Activity_date>/', Update_machinery_activities, name='update-machineryactivities'),

    path('show_machinerymaintenance/<str:Number_plate>/', Show_machinery_maintenance, name='show-machinerymaintenance')
]
