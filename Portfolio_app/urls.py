from django.urls import path
from Portfolio_app import views

urlpatterns = [
    path("",views.first,name="first"),
    path("form/",views.form,name="form"),
    path("main/",views.main,name="main"),
    path("mywork/",views.mywork,name="mywork")
]