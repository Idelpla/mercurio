from django.urls import path
from .views import StatementList, StatementNew

app_name = 'statements'

urlpatterns = [
    path('list', StatementList.as_view(), name='list'),
    path('new', StatementNew.as_view(), name='new'),
]
