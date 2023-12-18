from django.contrib import admin
from .models import Article, ArticleCategories, Career, Department, Job, Project, ProjectImages, JobType
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'body': CKEditorUploadingWidget(),  
        }

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'body': CKEditorUploadingWidget(),  
        }

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ("id", "author", "title", "date_added")
    search_fields = ("title", "slug", "body", "categories")
    readonly_fields = ('slug', 'author')  

    def save_model(self, request, obj, form, change):
        if not obj.pk and not obj.author:  # If it's a new object and author is not set
            obj.author = request.user.username  # Set author to current user's username
        super().save_model(request, obj, form, change)



class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

# Register your models with their respective ModelAdmin class
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategories)
admin.site.register(Career)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImages)
admin.site.register(JobType)
