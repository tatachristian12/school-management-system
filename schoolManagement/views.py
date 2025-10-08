from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Management, Announcement
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
    user_instance = User.objects.get(email=request.user.email)
    teacher_instance = Management.objects.get(user=user_instance)
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("announcement")
        if title and text:
            Announcement.objects.create(user=teacher_instance, title=title, announcement=text)
            messages.success(request, "Announcement created successfully!")
        else:
            messages.error(request, "Both title and announcement cannot be empty.")
        return redirect('/teacher-announcement')

    announcements = Announcement.objects.filter(user=teacher_instance, status=True).order_by('-created_at')
    data = {
        "teacher_instance": teacher_instance,
        "announcements": announcements
    }
    return render(request, "teacher/announcement.html", context=data)

def teacherAnnouncementDetail(request, ann_id):
    user_instance = User.objects.get(email=request.user.email)
    teacher_instance = Management.objects.get(user=user_instance)
    announcement = get_object_or_404(Announcement, id=ann_id,user=teacher_instance, status=True)
    data={
        "teacher_instance": teacher_instance,
        "announcement": announcement
    }
    return render(request, "teacher/announcementBody.html", context=data)
def editTeacherAnnouncement(request, ann_id):
    user_instance = User.objects.get(email=request.user.email)
    teacher_instance = Management.objects.get(user=user_instance)
    announcement = get_object_or_404(Announcement, id=ann_id, user=teacher_instance, status=True)

    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("announcement")
        if title and text:
            announcement.title = title
            announcement.announcement = text
            announcement.save()
            messages.success(request, "Announcement updated successfully!")
            return redirect(f'/teacher-announcement/{ann_id}/')
        else:
            messages.error(request, "Both title and announcement cannot be empty.")
            return redirect(f'/teacher-announcement/edit/{ann_id}/')

    data = {
        "teacher_instance": teacher_instance,
        "announcement": announcement
    }
    return render(request, "teacher/editAnnouncement.html", context=data)

def deleteTeacherAnnouncement(request, ann_id):
    user_instance = User.objects.get(email=request.user.email)
    teacher_instance = Management.objects.get(user=user_instance)
    announcement = get_object_or_404(Announcement, id=ann_id, user=teacher_instance)
    if request.method == "POST":
        announcement.status = False
        announcement.save()
        messages.success(request, "Announcement deleted successfully!")
        return redirect('/teacher-announcement')

    data = {
        "teacher_instance": teacher_instance,
        "announcement": announcement
    }
    return render(request, 'teacher/deleteAnnouncement.html', context=data)

    
def teacherEditProfile(request,teacher_id):
    user_instance = User.objects.get(email=request.user.email)  
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

def adminManageStudentAccount(request):
    return render(request, 'schAdmin/manageStudentAccount.html')

def adminStaffAccounts(request):
    return render(request, 'schAdmin/staffAccounts.html')

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