from django.shortcuts import render

# Create your views here.
def parentProfile(request):
    return render(request, 'parent/profile.html')

def parentAttendance(request):
    return render(request, 'parent/attendance.html')

def parentResults(request):
    return render(request, 'parent/results.html')

def editParentProfile(request):
    return render(request, 'parent/editProfile.html')

def updateParentProfile(request):
    pass