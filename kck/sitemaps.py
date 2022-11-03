from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from kck2021.models import Article

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'
 
    def items(self):
        return Article.objects.all()
    
    def lastmod(self, obj):
        return obj.date_added
    
    def location(self, obj):
        return '/blog/%s' % (obj.slug)

class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'
 
    def items(self):
        return ['kck:index', 'kck:contact', 'kck:about', 'kck:services', 'kck:project', 'kck:career', 'kck:project'] 
 
    def location(self, item):
        return reverse(item) #returning the static pages URL; home and contact us