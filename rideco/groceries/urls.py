from django.urls import path
from . import views

app_name = 'groceries'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createView.as_view(), name='create'),
    path('createList/', views.createList, name='createList'),
    path('updateList/', views.updateList, name='updateList'),
    path('<int:pk>/list/', views.listView.as_view(), name='list'),
]