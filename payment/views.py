from django.shortcuts import render

# Create your views here.
def managePayment(request):
    return render(request, 'payment/managePayment.html')

def makePayment(request):
    pass