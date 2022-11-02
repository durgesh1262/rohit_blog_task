from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class BlogApplicationCreationModel(models.Model):
    title = models.CharField(max_length=100, unique= True)
    slug = models.SlugField('slug', unique= True)
    # slug = AutoSlugField(populate_from = 'title',unique= True,null=True, default = None )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now = True)
    content= models.TextField()
    created_on = models.DateTimeField()
    STATUS_CHOICES = (
        ('1', 'Draft'),
        ('2', 'Publish'),
    )
    status = models.CharField(max_length=100, choices = STATUS_CHOICES, default = '1')
   
    
    def __str__(self):
        return self.title
    
    
    
        
