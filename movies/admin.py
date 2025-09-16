from django.contrib import admin
from .models import Movie, Review, MovieRequest

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)

class MovieRequestAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'user', 'date_requested']
    list_filter = ['date_requested', 'user']
    search_fields = ['movie_name', 'user__username']
    ordering = ['-date_requested']
admin.site.register(MovieRequest, MovieRequestAdmin)
