from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('show',views.show,name='show'),
    path('delete',views.delete,name='delete')
]
