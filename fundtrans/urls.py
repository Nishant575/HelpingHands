from django.urls import path
from . import views
from .views import TransListView

urlpatterns = [
    path('transfer/<int:pk>/',views.transfer, name='transfer'),
    path('transactions/', TransListView.as_view() , name='transactions'),

]