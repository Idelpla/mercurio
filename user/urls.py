from django.urls import path
from .views import Dashboard, Login

app_name = 'users'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('login', Login.as_view(), name='login'),
]
