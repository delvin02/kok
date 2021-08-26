from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategories, Career, Department, Job, Project
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

def servicesType(request, service_id):
    if service_id == 1:
        return render(request, "kck2021/services_welding.html")
    elif service_id == 2:
        return render(request, "kck2021/services_concrete.html")
    elif service_id == 3:
        return render(request, "kck2021/services_construction.html")

def contact(request):
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
    post = Article.objects.filter(slug=slug_name)
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

def enquiry(request):
    messageContent = request.POST.get("message")
    message_subject = request.POST.get("subject")
    sender_name = request.POST.get("name")
    sender_email = request.POST.get("email")
    sender_number = request.POST.get("phoneNumber")

    if messageContent and message_subject and sender_name and sender_name and sender_number:
        concat = messageContent + ' WHATSAPP NUMBER: ' + sender_number    
        email = EmailMessage(message_subject, concat, "kckokengineering@gmail.com", [sender_email], ['kckokengineering@kckok.my'])
        email.content_subtype='html'
        try:
            email.send(fail_silently=True)
        except BadHeaderError:
            return HttpResponse("Invalid Header Found.")
        return render(request, "kck2021/contact.html", {
            "sender_name": sender_name
        })
    else:
        return render(request, "kck2021/contact.html", {
            "failed": True
        })

def project(request):
    projects = Project.objects.all()
    return render(request, "kck2021/project.html", {
        "projects": projects
    })

def readproject(request, slug_title):
    readProject = Project.objects.filter(slug=slug_title)
    return render(request, "kck2021/projectbase.html", {
        "readProject": readProject,
    })