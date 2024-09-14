from django.shortcuts import render
from django.views import View

# Create your views here.

class LandingPage(View):
    def get(self , request):
        return render(request,'index.html')
    
class About(View):
    def get(self , request):
        return render(request , 'about.html')
    
class ProjectsView(View):
    def get(self , request):
        return render(request , 'work.html')
    
class SkilsView(View):
    def get(self , request):
        return render(request , 'category.html')