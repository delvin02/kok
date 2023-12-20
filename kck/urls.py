from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve 
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, BlogSitemap 
from django.views.generic.base import TemplateView

# Add sitemaps
sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("kck2021.urls", namespace='kck')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), 
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]
