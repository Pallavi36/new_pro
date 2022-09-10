from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Student,Book
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
def home(request):
    std=Student.objects.all()
    return render(request,"index.html",{'std':std})
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        rpassword=request.POST['rpassword']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'username already exits')
            return redirect("/signup")
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already exits')
            return redirect("/signup")
        elif password!=rpassword:
            messages.error(request,'passwords missmatch')
            return redirect("/signup")
        else:
            user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
            user.save()
            return redirect("/")
            messages.success(request,"sucessfully signed up")      
    else:
        return render(request,'signup.html')
def ulogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.warning(request,'Invalid user name and password')
            return redirect('/login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    messages.warning(request,'sucessfully logout')
    return redirect('/')
def addbook(request):
    if request.method=='POST':
        b=Book()
        b.name=request.POST['name']
        b.author=request.POST['author']
        b.language=request.POST['language']
        b.issuedby=request.POST['issuedby']
        b.save()
        messages.success(request,'sucessfully added')
        return redirect("/")
    else:
        return render(request,'addbook.html')
def showbooks(request):
    data=Book.objects.all()
    return render(request,'showbooks.html',{'std':data})
def delete(request):
    id=request.GET['id']
    Book.objects.filter(id=id).delete()
    data=Book.objects.all()
    return render(request,'showbooks.html',{'std':data})
def update(request):
    b=Book()
    b.id=request.POST['id']
    b.name=request.POST['name']
    b.author=request.POST['author']
    b.language=request.POST['language']
    b.issuedby=request.POST['issuedby']
    b.save()
    data=Book.objects.all()
    return render(request,'showbooks.html',{'std':data})


