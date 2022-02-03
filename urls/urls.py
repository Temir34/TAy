from django.contrid import admin
from django.urls import path,include
from django.conf import settings 

urlpatterns = [
    path('custom_admin',admin.site.urls),
    path('',include('firstapp.urls'))
]