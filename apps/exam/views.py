from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime

# Create your views here.
def login_page(request):
	return render(request, "exam/login_page.html")


def login(request):
	if request.method != "POST":
		return redirect("login_page")

	user = User.objects.filter(email=request.POST["email"])
	if not user:
		messages.info(request, "not a username")
		return redirect("login_page")
	
		#check= User.objects.get(username=request.POST["username"])
	check= User.usermanager.login(request.POST["email"], request.POST['password'])
	if check:
		user= User.objects.get(email= request.POST["email"])
		request.session["id"] = user.id
		return redirect("appoint")
	else:
		messages.info(request, 'Incorrect Password')
		return redirect("login_page")

def register(request):
	if request.method != "POST":
		return redirect("login_page")

	user = User.objects.filter(email=request.POST["email"])
	if user:
		return redirect("login_page")
	else:
		new=User.usermanager.register(name=request.POST["name"], email=request.POST["email"],password=request.POST["password"], confirmation=request.POST["confirmation"])
		if new[0]== False:
			messages.info(request,new[1])
		return redirect("login_page")	
		#user = User.objects.create(name=request.POST["name"], password=request.POST["password"], username=request.POST["username"])

	request.session["id"] = user.id

	return redirect("travels")

def appoint(request):
	if "id" not in request.session:
		return redirect("login_page")

	#print request.session['id']
	today= datetime.now().date()
	user= User.usermanager.get(id=request.session['id'])
	appoint= Appoint.appointmanager.filter(appointment=request.session['id']).exclude(date=today)
	todays= Appoint.appointmanager.filter(date=today, appointment=request.session['id'])
	#appoint= Appoint.appointmanager.filter(appointment=request.session['id']).exclude(date>07)
	

	#print appoint.tasks

	#print user.name
	#appoint= Appoint.appointmanager.get(id= request.session['id'])
	#print appoint
	#print appoint.name
	context= {
	"users": user, "appoints": appoint, "todays": todays, 'today': today

	}
	return render(request, "exam/appoint.html",context)
def add(request):
	return render(request,"exam/add.html")
def create(request):
	user= User.objects.get(id=request.session['id'])
	#check=Appoint.appointmanager.valid(request.POST['tasks'])
	#if check:
		#messages.info(request, 'Empty Task')
	Appoint.objects.create(date=request.POST["date"], time=request.POST["time"], tasks=request.POST["tasks"], appointment=user)
	return redirect('appoint')

def edit(request,id):
	if "id" not in request.session:
		return redirect("login_page")

	context={
	"id": id
	}
	return render(request, 'exam/edit.html',context) 	

def update(request,id):
	print id
	today= datetime.now().date()
	#if today == request.POST['date']:
		#print "cool"
	check=Appoint.appointmanager.valid(request.POST['tasks'])	
	#check=Appoint.appointmanager.valid(request.POST['tasks'],request.POST['date'], request.POST['time'], today)
	#print check
	if request.method== 'POST':
		if request.POST['status']== 'Pending':
				status= 'pending'
		if request.POST['status']== "Missed":
				status= 'missed'
		if request.POST['status']== "Done":
				status= 'done'		

		Appoint.objects.filter(id=id).update(tasks=request.POST['tasks'], date= request.POST['date'], time=request.POST['time'], status=status)
		#print appoint.date
		#appoint.objects
		#appoint.save()
	return redirect('appoint')	

def delete(request,id):
	print "is it getting here"
	Appoint.appointmanager.filter(id=id).delete()
	return redirect('appoint')					 	

def logout(request):
	request.session.clear()
	return redirect("login_page")	