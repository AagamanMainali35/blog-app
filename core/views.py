from django.shortcuts import render
from core.models import *
# Create your views here.
def home(request):
    data=blog.objects.all()
    context={'data':data}
    return render(request,'home.html',context)