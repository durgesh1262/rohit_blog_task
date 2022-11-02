from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BlogAppForm 
from django.utils.text import slugify 
from .models import *

 
 
def adddata(request):
    form = BlogAppForm() 
    if request.method == 'POST':
        form = BlogAppForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            form.save()
            fm =  BlogApplicationCreationModel.objects.all()
            return render(request, 'index.html', {'form':fm})  
    else:
        form = BlogAppForm() 
    return render(request, 'base.html', {'form': form})  

def displayblog(request, slug):
    if request.method == 'POST':
        pi =  BlogApplicationCreationModel.objects.get(slug = slug)
        fm = BlogAppForm(request.POST, instance=pi)
        if fm.is_valid():
            
            fm.save()
            return render(request, 'index.html', {'form':fm}) 
    else:
        pi =  BlogApplicationCreationModel.objects.get(slug = slug)
        fm = BlogAppForm(request.POST, instance=pi) 
    return render(request,'base.html',{'form':fm})    
               
def deleteblog(request, slug):
    if request.method == "POST":
        pi = BlogApplicationCreationModel.objects.get(slug = slug)     
        pi.delete()  
        return HttpResponseRedirect('/')         
            


     
               


