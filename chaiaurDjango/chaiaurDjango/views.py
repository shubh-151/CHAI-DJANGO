from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    #return HttpResponse("heloo wolrd achai ayur home ")
    return render(request, 'website\index.html')

def about(request):
    #return HttpResponse("heloo wolrd achai ayur about ")
    return render(request,r'website\about.html')

def contact(request):
    #return HttpResponse("heloo wolrd achai ayur contact ")
    return render(request,'website\contact.html')

