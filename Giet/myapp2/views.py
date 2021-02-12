from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stat(request):
	return HttpResponse("<center><h1 style='background-color:orange;margin-left:30%;margin-right:30%;padding:30px'>I am from app2</h1></center>")
def home(request):
	return HttpResponse("<center><h1 style='background-color:violet;margin-left:20%;margin-right:20%;padding:35px'>I am from app2 and my urls</h1></center>")
 
def index(request):
    return render(request,'index.html')
def student(request):
    details={'name':'gopi','number':44,'branch':'cse'}  
    return render(request,'studentinfo.html',{'details':details})  
def integer(request,pin):
    return  render(request,'pin.html',{"pin":pin})  
def table(request,v):
	a=[]
	for i in range(1,11):
		a.append(i*v)
	return render(request,'table.html',{'array':a,'v':v}) 
def sample(request):
    return render(request,"sample.html")	
def register(request):
	if request.method =='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		mail = request.POST.get('mail')
		password=request.POST.get('password')
		context={'fname':fname,'lname':lname,'mail':mail,'password':password}
		return render(request,'result.html',context)
	return render(request,'register.html')    
