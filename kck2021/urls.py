from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


app_name = "kck"
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/img/logo/favicon.ico'))),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path("voucher", views.voucher, name="voucher"),
    path("services/<str:service_name>/", views.servicesType, name="services"),
    
    # Policies
    path("services/semix/terms-and-conditions", views.semix_terms, name="semix_terms"),
    path("services/semix/whistle-blowing-policy", views.semix_whistle, name="semix_whistle"),

    path("blog", views.blog, name="blog"),
    path("blog/category=<str:category>", views.catBlog, name="catBlog"),
    path("blog/<slug:slug_name>", views.readblog, name="readblog"),
    path("career", views.career, name="career"),
    path("project", views.project, name="project"),
    path("project/<slug:slug_title>", views.readproject, name="readproject"),
    path("404", views.error, name="error"),
    path("robots.txt", views.robots_txt),

    path('terms/<str:company_name>/<slug:slug>/', views.legal_with_company, name='legal_with_company'),

    path('terms/<slug:slug>/', views.legal_without_company, name='legal_without_company')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'kck2021.views.error'
