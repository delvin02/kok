from django.contrib import admin
from .models import Article, ArticleCategories, Career, Department, Job, Project, ProjectImages, JobType, LegalCategory, Company, Legal, IdentityStatus, IdentityRegister, IdentityRegisterChangeLog
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.db import IntegrityError
from django.utils.text import slugify
from django.utils.html import format_html
from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError
from django.contrib import messages


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


class IdentityRegisterForm(forms.ModelForm):
    class Meta:
        model = IdentityRegister
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        statuses = cleaned_data.get('statuses')
        verified = cleaned_data.get('verified')

        if verified and not statuses.filter(status="Pengesahan selesai").exists():
            error_message = gettext_lazy("'Pengesahan selesai' must be included in statuses if verified is True.")
            self.add_error('statuses', error_message)

        return cleaned_data
    
class IdentityRegisterAdmin(admin.ModelAdmin):
    form = IdentityRegisterForm

    list_display = ("reference_code", "name", "phone" , "created", "get_statuses", "verified", "changed_by")
    search_fields = ("reference_code", "phone", "name", "verified")
    
    fields = ("phone", "front", "back", "selfie", "name","statuses", "verified")

    def get_statuses(self, obj):
        return ", ".join([status.status for status in obj.statuses.all()])
    get_statuses.short_description = 'Statuses'

    def changed_by(self, obj):
        latest_change = IdentityRegisterChangeLog.objects.filter(identity_register=obj).order_by('-timestamp').first()
        return latest_change.user.username if latest_change else "Unknown"
    changed_by.short_description = 'Changed By'


    def save_model(self, request, obj, form, change):
        
        obj.save()
        if change:  # If the object is being edited
            # Log the change and the user who made it
            IdentityRegisterChangeLog.objects.create(identity_register=obj, user=request.user)
            change_message = f"Changed by {request.user.username}"
            admin.ModelAdmin.log_change(self, request, obj, change_message)
        else:  # If the object is being added
            # Log the addition and the user who made it
            IdentityRegisterChangeLog.objects.create(identity_register=obj, user=request.user)
            change_message = f"Added by {request.user.username}"
            admin.ModelAdmin.log_addition(self, request, obj, change_message)

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
admin.site.register(IdentityStatus)
admin.site.register(IdentityRegister, IdentityRegisterAdmin)