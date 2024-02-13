from django.urls import  path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index_page, name="index"),
    path("linksubmit",views.submit, name ="submit"),
    path("<str:pixel>",views.download, name = "download"),
]