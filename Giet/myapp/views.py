from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def static(request):
	return HttpResponse("<center><h1 style='background-color:red;margin-left:40%;margin-right:40%;padding:12px;border-radius:12px;'>This is red</h1>" )
def dynamicstr(request,name):
    return HttpResponse("<center><h1 style='background-color:rgba(126,33,3,0.4);margin-left:30%;margin-right:30%;padding:15px;border-radius:13px;'>this is dynamic"+" "+name+" "+"<br> page</h1></center>")	
def dynamicint(request,roll):
    return HttpResponse("<center><h1> my pin number is: {}</h1></center>".format(roll))
def dynamicboth(request,n,name):
    return HttpResponse("<center><h1 style='background-color:rgba(76,45,66,0.8);margin-left:30%;margin-right:30%;padding:15px;border-radius:15px;'>my name is "+name+"<br>  and my number: {}</h1></center>".format(n))     
