from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

    
def list(request):
    return render(request,'list.html')

def bestphoto(request):
    return render(request,'bestphoto.html')

    
def recommend(request):
    return render(request,'recommend.html')

    
def enroll(request):
    return render(request,'enroll.html')

def login(request):
    return render(request,'login.html')

    
def join(request):
    return render(request,'join.html')

def photographer(request):
    return render(request,'photographer.html')

def product(request):
    return render(request,'product.html')

def upload(request):
    return render(request,'upload.html')

    
def reservation(request):
    return render(request,'reservation.html')

    
def history(request):
    return render(request,'history.html')

    
def favorite(request):
    return render(request,'favorite.html')

    
def mymodify(request):
    return render(request,'mymodify.html')

    
def bye(request):
    return render(request,'bye.html')
