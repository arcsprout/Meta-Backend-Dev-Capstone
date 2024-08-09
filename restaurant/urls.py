from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('items', MenuItemsView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
]