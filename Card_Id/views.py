from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Card_Id.models import Virtual_Id

# Create your views here.
def virtual_Id(request, Name):
    allPosts=get_object_or_404(Virtual_Id, Name=Name)
    # print(allPosts)
    context={'allPosts':allPosts}
    return render (request,'index.html',context)