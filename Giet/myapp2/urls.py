from django.urls import path
from myapp2 import views
urlpatterns = [
 path("homeurl/",views.home,name="home"),
 path("index/",views.index,name="index"),
 path("student/",views.student,name="student"),
 path("<int:pin>",views.integer,name="integer"),
 path("table/<int:v>",views.table,name="table"),
 path("sample1/",views.sample,name="sample"),
 path("register1/",views.register,name="register"),
]
