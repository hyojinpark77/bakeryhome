from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'homepage/index.html')

def login(request):
    return render(request,'homepage/login.html')

def join(request):
    return render(request,'homepage/join.html')

def new_product(request):
    return render(request,'homepage/new_product.html')
