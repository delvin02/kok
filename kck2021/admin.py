from django.contrib import admin
from .models import ArticleCategories, Article, Career, Department, Job, Project, ProjectImages


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "date_added", "categories")

@admin.register(ArticleCategories)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields =("title", "slug", "body", "categories")
    
    class Meta:
        model = Article
        exclude = ['updated_date']

admin.site.register(Career)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(ProjectImages)
admin.site.register(Project)

