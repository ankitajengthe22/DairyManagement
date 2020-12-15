from .models import Vendor, Milkentry
import datetime
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def dologin(request):
  usern=request.POST.get("username")
  passw=request.POST.get("password")
  user=authenticate(request, username=usern, password=passw)
  if user:
   login(request, user)
   flag=redirect('index')
  else:
   flag=redirect('loginpage')
  return flag


def logout_view(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='/loginpage')
def index(request):
	vendor=Vendor.objects.all()
	dict1={'vendor':vendor}
	return render(request,'index.html',dict1)


def loginpage(request):
	vendor=Vendor.objects.all()
	dict1={'vendor':vendor}
	return render(request,'login.html',dict1)


@login_required(login_url='loginpage')
def savevendor(request):
	name=request.POST.get('namef')
	print(name)
	contact=request.POST.get('contactf')
	print(contact)
	res=Vendor(name=name, contact=contact )
	res.save()
	return render(request, 'index.html' , {'alert':'registered succesfully'})

@login_required(login_url='loginpage')
def vendorlist(request):
	vendor=Vendor.objects.all()
	dict1={'vendor':vendor}
	return render( request ,'vendorlist.html' , dict1)

@login_required(login_url='loginpage')
def updvendor(request ,id):
    vendor = Vendor.objects.get(id=id)
    dict1 = {'vendor':vendor}
    return render(request,'updvendor.html',dict1)

@login_required(login_url='loginpage')
def updatevendor(request):
    id1=request.POST.get('id')
    name=request.POST.get('namef')
    contact=request.POST.get('contactf')
    res=Vendor.objects.filter(id=id1).update(name=name,contact=contact)
    return redirect("vendorlist")

@login_required(login_url='loginpage')
def delvendor(request,id):
	Vendor.objects.filter(id=id).delete()
	return redirect("vendorlist")

@login_required(login_url='loginpage')
def milkdataentry(request):
	id1=request.POST.get('id')
	obj=Vendor.objects.get(id=id1)
	name=obj.name
	date=request.POST.get('date')
	milktype=request.POST.get('milktype')
	quantity=request.POST.get('quantity')
	fat=request.POST.get('fat')
	snf=request.POST.get('snf')
	bill=float(quantity)*1/2*float(fat)+1/3*float(quantity)*float(snf)
	res=Milkentry(name=name,date=date ,milktype=milktype,quantity=quantity,fat=fat,snf=snf,bill=bill)
	res.save()
	return redirect("vendorlist")

@login_required(login_url='loginpage')
def detailsvendor(request ,name):
	obj=Milkentry.objects.filter(name=name).all()
	total=0
	for i in obj:
		total=total+i.bill
		print(i.date)
	print(total)
	dict1={'obj':obj,'obj1':total,'name':name}
	return render(request,'detailsvendor.html',dict1)

def vendorinterface(request):
	id=request.POST.get('id')
	ob = Vendor.objects.filter(id=id)
	for i in ob:
		name=i.name
	obj=Milkentry.objects.filter(name=name).all()
	total=0
	for i in obj:
		total=total+i.bill
	print(total)
	name=name.upper()
	dict1={'obj':obj,'obj1':total,'name':name}
	return render(request,'vendorinterface.html',dict1)



@login_required(login_url='loginpage')
def pay(request):
	name=request.POST.get('name')
	total=request.POST.get('total')
	date=request.POST.get('date')
	total=float(total)
	paymoney=request.POST.get('paymoney')
	paymoney=float(paymoney)
	bill=total-paymoney
	milktype='none'
	quantity=0.0
	fat=0.0
	snf=0.0
	Milkentry.objects.filter(name=name).all().delete()
	res=Milkentry(name=name,date=date , milktype=milktype , quantity=quantity , fat=fat , snf=snf , bill=bill)
	res.save()
	return render(request,'index.html')



