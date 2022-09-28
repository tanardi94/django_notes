from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-member/', views.add, name='add_member'),
    path('add-member/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.deleteRecord, name='delete_record')
]
