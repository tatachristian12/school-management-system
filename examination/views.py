from django.shortcuts import render

# Create your views here.
def manageExam(request):
    return render(request, 'examination/manageExam.html')

def saveExamResults(request):
    pass

def editExamResults(request):
    pass

def updateExamResults(request):
    pass