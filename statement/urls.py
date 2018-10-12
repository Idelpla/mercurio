from django.urls import path
from .views import StatementList, StatementNew, StatementDetail

app_name = 'statements'

urlpatterns = [
    path('list', StatementList.as_view(), name='list'),
    path('new', StatementNew.as_view(), name='new'),
    path('detail/<int:pk>', StatementDetail.as_view(), name='detail'),
]
