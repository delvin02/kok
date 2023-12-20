from django.contrib import admin
from .models import Article, ArticleCategories, Career, Department, Job, Project, ProjectImages, JobType, LegalCategory, Company, Legal
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.db import IntegrityError
from django.utils.text import slugify
from django.utils.html import format_html


class MyAdminSite(admin.AdminSite):
    site_header = 'My Administration'
    # ... other custom settings ...

admin_site = MyAdminSite(name='KCK Group')

def duplicate_model(modeladmin, request, queryset):
    for original_object in queryset:
        original_object.id = None  # setting 'id' to None creates a new instance

        # Handle the title field
        counter = 1
        original_title = original_object.title
        new_title = f"{original_title} (Copy {counter})"
        while Legal.objects.filter(title=new_title).exists():
            counter += 1
            new_title = f"{original_title} (Copy {counter})"

        original_object.title = new_title
        original_object.save()

duplicate_model.short_description = "Duplicate selected items"

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'body': CKEditorUploadingWidget(),  
        }

class LegalAdminForm(forms.ModelForm):
    class Meta:
        model = Legal
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
    view_on_site = True

    def save_model(self, request, obj, form, change):
        if not obj.pk and not obj.author:  # If it's a new object and author is not set
            obj.author = request.user.username  # Set author to current user's username
        super().save_model(request, obj, form, change)


class LegalAdmin(admin.ModelAdmin):
    form = LegalAdminForm
    list_display = ("id", "title", "category" ,"company", "created", "view_on_site_link")
    search_fields = ("title", "slug", "body", "category", "company")
    readonly_fields = ('slug', )  
    actions = [duplicate_model]

    view_on_site = True

    def view_on_site_link(self, obj):
        return format_html('<a href="{}">View</a>', obj.get_absolute_url())
    view_on_site_link.short_description = 'View on Site'

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
admin.site.register(Legal, LegalAdmin)
admin.site.register(Company)
admin.site.register(LegalCategory)