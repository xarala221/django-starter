from django.shortcuts import render

# Create your views here.

def index(request):
  title = "Welcome to my website"
  return render(request, "myapp/index.html", {"title": title})