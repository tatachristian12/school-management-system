from django.shortcuts import render, HttpResponse, redirect
from .models import Management
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def teacherProfile(request):
    user_instance = User.objects.get(email=request.user.email)  # now using custom user
    teacher_instance = Management.objects.get(user=user_instance)

    data = {
        "teacher_instance": teacher_instance
    }

    return render(request, 'teacher/profile.html', context=data)

def teacherCourse(request):
    return render(request, 'teacher/courses.html')

def teacherAttendance(request):
    return render(request, 'teacher/attendance.html')

def teacherAnnouncement(request):
    return render(request, 'teacher/announcement.html')

def teacherEditProfile(request,teacher_id):
    user_instance = User.objects.get(email=request.user.email)  # now using custom user
    teacher_instance = Management.objects.get(user=user_instance)

    data = {
        "teacher_instance": teacher_instance,
        "teacher_id" : teacher_id
    }
    return render(request, 'teacher/editProfile.html',context=data)

def teacherUpdateProfile(request,teacher_id):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        address = request.POST['address']
        marital_status = request.POST['marital_status']
        DOB = request.POST['DOB']
        user_instance = User.objects.get(email=request.user.email)
        user_instance.first_name = first_name
        user_instance.last_name = last_name
        user_instance.email = email
        user_instance.username = username
        user_instance.save()
        teacher_instance = Management.objects.get(user=user_instance)
        teacher_instance.address = address
        teacher_instance.marital_status = marital_status
        teacher_instance.DOB = DOB
        teacher_instance.save()
        messages.success(request, "profile updated successfully")
        return redirect(f'/edit-teacher-profile/{teacher_id}')  
    else:
        messages.success(request, "Fail to Update")
        return redirect(f'/edit-teacher-profile/{teacher_id}')  

def teacherAddCourse(request):
    pass

def updateAttendanceRecord(request):
    pass

def adminProfile(request):
    user_instance = User.objects.get(email=request.user.email)  # now using custom user
    admin_instance = Management.objects.get(user=user_instance)

    data = {
        "admin_instance": admin_instance
    }
    return render(request, 'schAdmin/profile.html', context=data)

def adminUserManagement(request):
    if request.user.is_authenticated:
        user_instance = User.objects.get(email=request.user.email)  # now using custom user
        admin_instance = Management.objects.get(user=user_instance)
        current_user = request.user
        all_users = User.objects.filter(status = True).exclude(pk = current_user.pk)
        active_users = True
        data = {
            "all_users": all_users,
            "active_users": active_users,
            "admin_instance": admin_instance
        }
        return render(request, 'schAdmin/userManagement.html', context=data)
    
def adminDeleteConfirmationPage(request, delete_id):
    fetchedUser = User.objects.get(id = delete_id)
    if fetchedUser:
        data = {
            "fetchedUser": fetchedUser,
        }
        return render(request, 'schAdmin/deleteConfirmationPage.html', context=data)
    else:
        messages.success(request, "No user Found")
        return redirect('/admin-user-management')

def adminSuspendConfirmationPage(request, suspend_id):
    fetchedUser = User.objects.get(id = suspend_id)
    if fetchedUser:
        data = {
            "fetchedUser": fetchedUser,
        }
        return render(request, 'schAdmin/suspendConfirmationPage.html', context=data)
    else:
        messages.success(request, "No user Found")
        return redirect('/admin-user-management')
    
def adminActivateConfirmationPage(request, activate_id):
    fetchedUser = User.objects.get(id = activate_id)
    if fetchedUser:
        data = {
            "fetchedUser": fetchedUser,
        }
        return render(request, 'schAdmin/activateConfirmationPage.html', context=data)
    else:
        messages.success(request, "No user Found")
        return redirect('/admin-user-management')
    
def adminDeleteUser(request, delete_id):
    if request.method == "GET":
        deleteUser = User.objects.filter(id = delete_id).update(status = False)
        if deleteUser:
            messages.success(request, "User deleted successfully.")
            return redirect('/admin-user-management')
        else:
            messages.success(request, "Unable to delete user.")
            return redirect('/admin-user-management')
    
def adminDeletedUsers(request):
    if request.user.is_authenticated:
        current_user = request.user
        all_users = User.objects.filter(status = False).exclude(pk = current_user.pk)
        all_deleted_users = True
        data = {
            "all_users": all_users,
            "all_deleted_users": all_deleted_users
        }
        return render(request, 'schAdmin/userManagement.html', context=data)
    
def adminActivateUsers(request, activate_id):
      if request.method == "GET":
        deleteUser = User.objects.filter(id = activate_id).update(status = True)
        if deleteUser:
                messages.success(request, "User Activated successfully.")
                return redirect('/admin-user-management')
        else:
            messages.success(request, "Unable to activate user.")
            return redirect('/admin-user-management')
        
def adminSuspendUsers(request, suspend_id):
    if request.method == "GET":
        deleteUser = User.objects.filter(id = suspend_id).update(status = "suspend")
        if deleteUser:
            messages.success(request, "User suspended successfully.")
            return redirect('/admin-user-management')
        else:
            messages.success(request, "Unable to delete user.")
            return redirect('/admin-user-management')
        
def adminSuspendedUsers(request):
    if request.user.is_authenticated:
        current_user = request.user
        all_users = User.objects.filter(status = "suspend").exclude(pk = current_user.pk)
        all_suspended_users = True
        data = {
            "all_users": all_users,
            "all_suspended_users": all_suspended_users
        }
        return render(request, 'schAdmin/userManagement.html', context=data)

def adminEditProfile(request,admin_id):
    user_instance = User.objects.get(email=request.user.email)  # now using custom user
    admin_instance = Management.objects.get(user=user_instance)

    data = {
        "admin_instance": admin_instance,
        "admin_id" : admin_id
    }
    return render(request, 'schAdmin/editProfile.html',context=data)

def adminUpdateProfile(request,admin_id):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        address = request.POST['address']
        marital_status = request.POST['marital_status']
        DOB = request.POST['DOB']
        user_instance = User.objects.get(email=request.user.email)
        user_instance.first_name = first_name
        user_instance.last_name = last_name
        user_instance.email = email
        user_instance.username = username
        user_instance.save()
        admin_instance = Management.objects.get(user=user_instance)
        admin_instance.address = address
        admin_instance.marital_status = marital_status
        admin_instance.DOB = DOB
        admin_instance.save()
        messages.success(request, "profile updated successfully")
        return redirect(f'/edit-admin-profile/{admin_id}')  
    else:
        messages.success(request, "Fail to Update")
        return redirect(f'/edit-admin-profile/{admin_id}')  