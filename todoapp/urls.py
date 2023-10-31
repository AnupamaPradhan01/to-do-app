from django.urls import path 
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("delete<int:id>/",views.delete,name="delete"),
    path("<int:id>/",views.update,name="update"),
    path("mark_complete<int:id>/",views.mark_complete,name="mark_complete"),
    path("mark_incomplete<int:id>/",views.mark_incomplete,name="mark_incomplete"),
    ]