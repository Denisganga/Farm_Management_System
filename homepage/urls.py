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
    Add_machinery
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
]
