from django.urls import path
from .views import Dashboard, Login, ElectronicAddress

app_name = 'users'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('login', Login.as_view(), name='login'),
    path('electronic-address', ElectronicAddress.as_view(), name='electronic_address'),
]
