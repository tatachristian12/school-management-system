from django.shortcuts import render, HttpResponse, redirect
from .models import Management
from .models import Courses, SchoolDepartment, Student
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def teacherProfile(request):
    user_instance = User.objects.get(email=request.user.email)   # now using custom user
    teacher_instance = Management.objects.get(user=user_instance)

    data = {
        "teacher_instance": teacher_instance
    }

    return render(request, 'teacher/profile.html', context=data)

def teacherCourse(request):
     department_id = request.GET.get('department')
     courses = Courses.objects.filter(teacher = request.user)
     if department_id:
         courses = courses.filter(department_id=department_id)

     departments = SchoolDepartment.objects.all()

     return render(request, 'teacher/courses.html', {
         "courses": courses,
         "departments": departments,
         "selectedDepartment": department_id
         })

def adminCourse(request):
    courses = Courses.objects.all()
    return render(request, 'schAdmin/courses.html', {
        "courses": courses
    })


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
    

def adminAddCourse(request):
    if request.method == "POST":
        name = request.POST['name']
        course_code = request.POST['course_code']
        course_value = request.POST['course_value']
        departmentId = request.POST.get('department')
        userId = request.POST.get('teacher')
        if not departmentId:
            messages.error(request, "Please Select A Department")
            return redirect('/admin-add-course')

        department = SchoolDepartment.objects.get(id = departmentId)
        teacher = User.objects.get(id = userId)

        Courses.objects.create(
            teacher = teacher,
            department = department,
            name = name,
            course_code = course_code,
            course_value = course_value,
        )
        messages.success(request, "Course created successfully!")
        return redirect('/admin-courses')
    else:
        departments = SchoolDepartment.objects.all()
        teachers = User.objects.filter(is_teacher = True)
        return render(request, "schAdmin/addCourse.html", {"departments": departments, "teachers": teachers})
      


def adminEditCourse(request, courseId):
        admin_instance = Management.objects.get(user=request.user)
        course = Courses.objects.get(id=courseId, teacher = request.user)
        departments = SchoolDepartment.objects.all()
        
        data = {
            "admin_instance": admin_instance,
            "teacher_id": admin_instance.id,
            "courseId": courseId,
            "course": course,
            'departments': departments,
        }
        return render(request, "schAdmin/editCourse.html", context=data)


def adminUpdateCourse(request, courseId):
    if request.method == "POST":
        name = request.POST['name']
        course_code = request.POST['course_code']
        course_value = request.POST['course_value']
        user_instance = User.objects.get(email = request.user.email)

        course = Courses.objects.get(id = courseId, teacher = user_instance)
        course.name = name
        course.course_code = course_code
        course.course_value = course_value
        course.save()
        messages.success(request, "Course Updated Successfully!")
        return redirect(f'/admin-courses')
    else:
        messages.error(request, "Failed To Update Course")
        return redirect(f'/edit-admin-course/{courseId}')
    
def adminDeleteCourse(request, courseId):
    Courses.objects.filter(id=courseId).delete()
    return redirect('/admin-courses')    

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