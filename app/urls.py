from django.urls import path
from . import views

urlpatterns = [
path('',views.index, name="home"),
path('addemp/',views.addemp,name="addemp"),
path('delete/<id>',views.delete, name="delete"),
path('update/<id>',views.update, name="update")
]
