from django.urls import path
from .views import Register, Login
from django.conf import settings
from django.conf.urls.static import static


app_name = "authentication"

urlpatterns = [
    path("register/", Register, name="register"),
    path("login/", Login, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
