from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from video.models import Movie, Customer


class MovieAdmin(admin.ModelAdmin):
    fields = ['released_year', 'title', 'length']
    
    search_fields = ['title']
    
    list_filter = ['released_year'] 
    
    list_display = ['title', 'released_year', 'length']
    
    list_editable = ['length']
    

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Customer)



