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

def mypage(request):
    return render(request,'mypage.html')

def photographer(request):
    return render(request,'photographer.html')

def product(request):
    return render(request,'product.html')

def upload(request):
    return render(request,'upload.html')
