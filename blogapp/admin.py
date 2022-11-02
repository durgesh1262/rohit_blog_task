from django.contrib import admin
from .models import BlogApplicationCreationModel


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title','slug','created_on', 'status')
    search_fields = ('title', 'content')
    list_filter = ['status']

admin.site.register(BlogApplicationCreationModel,BlogAdmin)




# Register your models here.
