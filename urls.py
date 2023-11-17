from django.urls import path 
from . import views 

urlpatterns =[
    path ("",views.home,name="home"),
    path ( "todos/",views.todos, name="Todos"),
     path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact")
]
 