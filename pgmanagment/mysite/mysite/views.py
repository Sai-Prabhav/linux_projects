from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
    return HttpResponse("Hello, world. You're at the polls index.")

def print_it(request,name):
    return render(request, 'good_print.html', {'print':name,'len':len(name),'list':[1,2,3]})

def page_render(request):
    return render(request, 'index.html')

def home(request):

    try:
        dat=request.POST
    except:
        pass
        
    # print(dict(dat),"------------------------------------------------------------")
    return render(request, 'home.html',dat)

def form_view(request):
    try:
        dat=request.POST
    except:
        dat={"val1":0,"val2":0}
    return render(request, 'form.html',dat)