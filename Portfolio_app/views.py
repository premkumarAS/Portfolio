from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,"first.html")
def main(request):
    return render(request,"main.html")
def form(request):
    return render(request,"form.html")
def mywork(request):
    return render(request,"mywork.html")