from django.shortcuts import render, HttpResponse

# Create your views here.
def studentProfile(request):
    return render(request, 'student/profile.html')

def studentCourse(request):
    return render(request, 'student/courses.html')

def studentAttendance(request):
    return render(request, 'student/attendance.html')

def studentAnnouncement(request):
    return render(request, 'student/announcement.html')

def studentFeeManagement(request):
    return render(request, 'student/feesManagement.html')

def finalResults(request):
    return render(request, 'student/finalResult.html')

def editProfile(request):
    return render(request, 'student/editProfile.html')

def updateProfile(request):
    pass
