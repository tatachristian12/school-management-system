from django.shortcuts import render, redirect





# Create your views here.
def teacherProfile(request):







    return render(request, 'teacher/profile.html')

def teacherCourse(request):
    return render(request, 'teacher/courses.html')

def teacherAttendance(request):
    return render(request, 'teacher/attendance.html')

def teacherAnnouncement(request):
    return render(request, 'teacher/announcement.html')

def teacherEditProfile(request):







    return render(request, 'teacher/editProfile.html')

def teacherUpdateProfile(request):























    return redirect()

def teacherAddCourse(request):
    pass

def updateAttendanceRecord(request):
    pass

def adminProfile(request):
    return render(request, 'schAdmin/profile.html')

def adminManageStudentAccount(request):
    return render(request, 'schAdmin/manageStudentAccount.html')

def adminStaffAccounts(request):
    return render(request, 'schAdmin/staffAccounts.html')
