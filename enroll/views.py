from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from enroll.models import Class
from enroll.form import stu
def crud(request):
    if request.method=="POST":
     f=stu(request.POST)
     if f.is_valid():
      nm=f.cleaned_data['Name']
      em=f.cleaned_data['email']
      pw=f.cleaned_data['password']
      reg=Class(Name=nm,email=em,password=pw)
      reg.save()
      f=stu()


    else:
     f=stu()
    s=Class.objects.all()
 
   
    return render(request,"home.html",{'f':f,'s':s})        
    
def delete(request,id):

  s=Class.objects.get(id=id)
  s.delete()
  return redirect('/')
def edit(request,id):
    s= Class.objects.get(id=id)  
    form = stu(request.POST, instance = s)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'editandupdate.html', {'s': s})

# Create your views here.
 