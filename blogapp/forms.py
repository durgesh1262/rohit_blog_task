from django import forms
from django.forms import ModelForm
from .models import BlogApplicationCreationModel

class BlogAppForm(forms.ModelForm):
    class Meta():
        model = BlogApplicationCreationModel
        # fields = ['title', 'slug', 'status', 'created_on']
        fields = '__all__'
        
        