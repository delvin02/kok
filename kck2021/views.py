from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse, FileResponse, Http404
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Article, ArticleCategories, Career, Department, Job, Project
from django.views.decorators.http import require_POST, require_GET

# Views for /robots.txt
@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Create your views here.
def index(request):
    latestBlog = Article.objects.all()[:2]
    projects = Project.objects.all()[:6]

    return render(request, "kck2021/index.html", {
        "latestBlog": latestBlog,
        "projects": projects,
    })

def about(request):
    posts = Article.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "kck2021/about.html", context)


def services(request):
    return render(request, "kck2021/services.html")

def servicesType(request, service_name):
    if service_name == "kimpalan":
        return render(request, "kck2021/services_welding.html")
    elif service_name == "semix":
        return render(request, "kck2021/services_concrete.html")
    elif service_name == "pembinaan":
        return render(request, "kck2021/services_construction.html")
    elif service_name == "pasir":
        return render(request, "kck2021/services_sand.html")
    elif service_name == "kren":
        return render(request, "kck2021/services_crane.html")
    elif service_name == "fabrikasi":
        return render(request, "kck2021/services_fabrication.html")

def contact(request):
    if request.method == "GET":
        return render(request, "kck2021/contact.html")


def blog(request):
    if 'search' in request.GET:
        search = request.GET['search']
        posts = Article.objects.filter(title__icontains=search) | Article.objects.filter(body__icontains=search)
    else:
        posts = Article.objects.all()
    
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    # this will act is list 
    pages = paginator.get_page(page)    
    nums = "a" * pages.paginator.num_pages
    categories = ArticleCategories.objects.all()
    # recent posts
    recent = Article.objects.all().order_by('?')[:5]
    return render(request, "kck2021/blog.html", {
        "pages": pages,
        "nums": nums,
        "categories": categories,
        "recent": recent,
    })

def catBlog(request, category):
    category = ArticleCategories.objects.get(category=category)
    posts = category.articleCategories.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    # this will act is list 
    pages = paginator.get_page(page)    
    nums = "a" * pages.paginator.num_pages

    categories = ArticleCategories.objects.all()
    recent = Article.objects.all().order_by('?')[:5]

    return render(request, "kck2021/blog.html", {
        "pages": pages,
        "categories": categories,
        "recent": recent,
        "nums": nums
    })

def readblog(request, slug_name):
    post = Article.objects.get(slug=slug_name)
    categories = ArticleCategories.objects.all()
    recent = Article.objects.all().order_by('?')[:5]
    return render(request, "kck2021/blogbase.html", {
        "post": post,
        "categories": categories,
        "recent": recent
    })
def career(request):
    jobs = Career.objects.all()

    return render(request, "kck2021/career.html", {
        "jobs": jobs
    })


def project(request):
    projects = Project.objects.all()
    return render(request, "kck2021/project.html", {
        "projects": projects
    })

def readproject(request, slug_title):
    project = Project.objects.get(slug=slug_title)
    return render(request, "kck2021/projectbase.html", {
        "project": project,
    })
def semix_terms(request):
    return render(request, "kck2021/semix-terms.html")

def semix_whistle(request):
    return render(request, "kck2021/semix-whistle.html")

def voucher(request):
    return render(request, "kck2021/voucher.html")

def error(request, exception):
    return render(request, "404.html", status=404)