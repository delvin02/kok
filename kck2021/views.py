from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import HttpResponse, FileResponse, Http404
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import *
from django.views.decorators.http import require_POST, require_GET
from .forms import IdentityRegisterForm
from .utils import generate_reupload_link

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
    elif service_name == "backhoe":
        return render(request, "kck2021/services_backhoe.html")
    elif service_name =="longarm":
        return render(request, "kck2021/services_longarm.html")
    elif service_name == "loadcovering":
        return render(request, "kck2021/services_loadcovering.html")
    
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
    if 'search' in request.GET:
        blog(request)
        
    post = Article.objects.get(slug=slug_name)
    categories = ArticleCategories.objects.all()
    recent = Article.objects.all().order_by('?')[:5]
    return render(request, "kck2021/blogbase.html", {
        "post": post,
        "categories": categories,
        "recent": recent
    })

def career(request):
    careers = Career.objects.all()
    return render(request, "kck2021/career.html", {
        "careers": careers
    })


def project(request):
    projects = Project.objects.all()
    return render(request, "kck2021/project.html", {
        "projects": projects
    })

def readproject(request, slug_title):
    project = Project.objects.get(slug=slug_title)
    images = ProjectImages.objects.filter(project=project)
    return render(request, "kck2021/projectbase.html", {
        "project": project,
        "images": images
    })
def semix_terms(request):
    return render(request, "kck2021/semix-terms.html")

def semix_whistle(request):
    return render(request, "kck2021/semix-whistle.html")

def voucher(request):
    return render(request, "kck2021/voucher.html")

def error(request, exception):
    return render(request, "404.html", status=404)

def legal_with_company(request, company_name, slug):
    legal = get_object_or_404(Legal, company__name__iexact=company_name, slug=slug)
    return render(request, 'kck2021/legal_detail.html', {'legal': legal})

def legal_without_company(request, slug):
    legal = get_object_or_404(Legal, slug=slug, company__isnull=True)
    return render(request, 'kck2021/legal_detail.html', {'legal': legal})

def identity_register(request):
    if request.method == 'POST':
        form = IdentityRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            reference_code = instance.reference_code
            return redirect('kck:identity_registered', reference_code=reference_code)  # Redirect to a success page
        else:
            return render(request, 'kck2021/identity_register.html', {'form': form})

    else:
        form = IdentityRegisterForm()
    return render(request, 'kck2021/identity_register.html', {'form': form})

def identity_registered(request, reference_code):
    identity = get_object_or_404(IdentityRegister, reference_code=reference_code)
    return render(request, 'kck2021/identity_registered.html', {'identity': identity})


def identity_register_status(request, reference_code):
    identity = get_object_or_404(IdentityRegister, reference_code=reference_code)
    return render(request, 'kck2021/identity_register_status.html', {'identity': identity})

def identity_reupload_request(request, reference_code):
    identity_register = get_object_or_404(IdentityRegister, reference_code=reference_code)
    try:
        # Attempt to find an existing, valid token
        reupload_token = ReuploadToken.objects.filter(identity_register=identity_register, expires_at__gt=timezone.now()).latest('expires_at')
    except ReuploadToken.DoesNotExist:
        # If no valid token exists, generate a new one
        link = generate_reupload_link(identity_register)
        return redirect(link)

    # If a valid token exists, redirect to the re-upload page with the existing token
    return redirect(reverse('kck:identity_reupload', kwargs={'token': reupload_token.token}))

def identity_reupload(request, token):
    # Attempt to find the token and ensure it's not expired
    reupload_token = get_object_or_404(ReuploadToken, token=token, expires_at__gt=timezone.now())
    
    # Get the associated IdentityRegister instance
    identity_register = reupload_token.identity_register

    if request.method == 'POST':
        form = IdentityRegisterForm(request.POST, request.FILES, instance=identity_register)
        if form.is_valid():
            identity = form.save()

            belum_disemak_status, created = IdentityStatus.objects.get_or_create(status="Belum disemak")
            identity.statuses.clear()
            identity.statuses.add(belum_disemak_status)

            reupload_token.delete()
            return render(request, 'kck2021/identity_registered.html', {'identity': identity})
    else:
        # Pre-fill the form with the existing IdentityRegister instance
        form = IdentityRegisterForm(instance=identity_register)
    
    # Render the re-upload form with the pre-filled data
    return render(request, 'kck2021/identity_register.html', {'form': form, 'token': token})