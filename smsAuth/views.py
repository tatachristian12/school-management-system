from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib import messages
from schoolManagement.models import *
from student.models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def createManageAccount(request):
    return render(request, 'auth/createManagementAccount.html')

def createStudentAccount(request):
    return render(request, 'auth/createStudentAccount.html')

    
@transaction.atomic
def createManagementAccountAuth(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
    
    if User.objects.filter(email = email).exists():
        messages.success(request, "User already exist.")
        return redirect('/create-account')
    
    if not User.objects.filter(email = email).exists():
        newUserInstance = User.objects.create_user(username = username, password = password, email = email, first_name = firstname, last_name = lastname)
        if newUserInstance:
            newUserInstance.save()
            newManagementInstance = Management(user = newUserInstance)
            newManagementInstance.save()
            messages.success(request, "Account created successfully")
            return redirect('/create-account')
        
        else:
            messages.success(request, "Something went wrong")
            return redirect('/create-account')
        
    else:
        messages.success(request, "Something went wrong")
        return redirect('/create-account')
    
@transaction.atomic
def createStudentAccountAuth(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        is_student = True
    
    if User.objects.filter(email = email).exists():
        messages.success(request, "User already exist.")
        return redirect('/create-account')
    
    if not User.objects.filter(email = email).exists():
        newUserInstance = User.objects.create_user(username = username, password = password, email = email, first_name = firstname, last_name = lastname, is_student = is_student)
        if newUserInstance:
            newUserInstance.save()
            newManagementInstance = Student(user = newUserInstance)
            newManagementInstance.save()
            messages.success(request, "Account created successfully")
            return redirect('/create-account')
        
        else:
            messages.success(request, "Something went wrong")
            return redirect('/create-account')
        
    else:
        messages.success(request, "Something went wrong")
        return redirect('/create-account')
        

def userLogin(request):
    return render(request, 'auth/login.html')

@transaction.atomic
def userAuthentication(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    
    if not User.objects.filter(username=username).exists():
        messages.success(request, "User does not exist.")
        return redirect('/')
    
    if User.objects.filter(username=username).exists():
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active and user.is_student:
                login(request, user)
                return redirect('/student-profile')
            if user.is_active and user.is_teacher:
                login(request, user)
                return redirect('/teacher-profile')
            if user.is_active and user.is_parent:
                login(request, user)
                return redirect('/parent-profile')
            if user.is_active and user.is_admin:
                login(request, user)
                return redirect('/admin-profile')
            else:
                messages.success(request, "Incorrect username or password.")
            return redirect('/')
        else:
            messages.success(request, "Incorrect username or password.")
            return redirect('/')

def userLogout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('/')

def resetPassword(request):
    return render(request, 'auth/resetPassword.html')