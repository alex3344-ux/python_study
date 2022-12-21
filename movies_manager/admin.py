from django.contrib import admin


# Register your models here.
from  .models import Movie, Director

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', )
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', )

class MovieAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'published_on', 'name', 'rating', )
    list_display_links = ('name',) 
    search_fields = ('name', 'rating')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)