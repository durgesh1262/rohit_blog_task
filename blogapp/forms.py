from django import forms
from django.forms import ModelForm
from .models import BlogApplicationCreationModel

class BlogAppForm(forms.ModelForm):
    class Meta():
        model = BlogApplicationCreationModel
        fields = ['title', 'author', 'created_on', 'status', 'content']
        

        # fields = '__all__'
        
        