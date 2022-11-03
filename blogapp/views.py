from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from .forms import BlogAppForm 
from django.utils.text import slugify 
from .models import BlogApplicationCreationModel

 
 
def adddata(request):
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
    return render(request, 'add.html', {'form': form})  

def tabledata(request):
    fm =  BlogApplicationCreationModel.objects.all()
    return render(request, 'index.html', {'form':fm})  

# for eding on data
def displayblog(request, slug):
    if request.method == 'POST':
        pi =  BlogApplicationCreationModel.objects.get(slug = slug)
        fm = BlogAppForm(request.POST, instance=pi)
        if fm.is_valid():
            
            fm.save()
            return HttpResponseRedirect('/blogapp/table/') 
            # return render(request, 'base.html', {'form':fm}) 
    else:
        pi =  BlogApplicationCreationModel.objects.get(slug = slug)
        fm = BlogAppForm(instance=pi) 
    return render(request,'display.html',{'form':fm})    
               
def deleteblog(request, slug):
    pi = BlogApplicationCreationModel.objects.get(slug = slug)     
    pi.delete()  
    return HttpResponseRedirect('/blogapp/table/')         
            


     
               


