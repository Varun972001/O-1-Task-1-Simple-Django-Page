from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "name":"Varun Jain"
    }
    return render(request,"task1.html",context)
