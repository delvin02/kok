from django.contrib import admin
from .models import ArticleCategories, Article, Career, Department, Job, Project

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "date_added", "categories")

@admin.register(ArticleCategories)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields =("title", "slug", "body", "categories")
    
    class Media:
        js=('tiny.js',)

admin.site.register(Career)
admin.site.register(Department)
admin.site.register(Job)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    class Media:
        js=('project.js',)
