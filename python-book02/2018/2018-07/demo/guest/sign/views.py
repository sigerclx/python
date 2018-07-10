from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request):
	#return HttpResponse('Hello diango!')
	return render(request,'index.html')

def login_action(request):
	if request.method =='POST':
		username =request.POST.get('username','')
		password = request.POST.get('password','')
		user =auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			#return render(request,'event_manage.html')
			reponse =HttpResponseRedirect('/event_manage/')
			#reponse.set_cookie('user',username,3600) #添加浏览器cookie
			request.session['user']=username   #将session记录到浏览器
			return reponse
		else:
			return render(request,'index.html',{'error':'username or password error!'})
# Create your views here.

@login_required
def event_manage(request):
	#username = request.COOKIES.get('user','') #读取浏览器cookie
	username =request.session.get('user','')	#读取浏览器sessionz
	return render(request,"event_manage.html",{"user":username})
