from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "kck"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path("services/<int:service_id>/", views.servicesType, name="services"),
    path("blog", views.blog, name="blog"),
    path("blog/category=<str:category>", views.catBlog, name="catBlog"),
    path("blog/<slug:slug_name>", views.readblog, name="readblog"),
    path("career", views.career, name="career"),
    path("project", views.project, name="project"),
    path("project/<slug:slug_title>", views.readproject, name="readproject")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)