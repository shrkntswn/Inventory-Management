from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('list-item', views.list_item, name='list_item'),
    path('add-item', views.add_item, name='add_item'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_item/<str:pk>/', views.delete_item, name="delete_item"),
]
