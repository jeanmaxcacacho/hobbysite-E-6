from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from merchstore.models import Transaction
from commissions.models import JobApplication
from wiki.models import Article as wikiArticle
from blog.models import Article as blogArticle


from user_management.models import Profile

# Create your views here.

def homepage_test(request):
    return HttpResponse("hello from homepage")


def homepage(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        profile = Profile.objects.filter(user=user).first()
    return render(
        request,
        "homepage/home.html",
        {
            "user": user,
            "profile": profile
        }
    )

"""
products bought & sold
commissions created and joined
wiki articles created
blog articles created

I'd rather have a clean view so I'll do the querying in the template itself
"""
@login_required
def dashboard(request):
    transactions = Transaction.objects.all()
    jobApplications = JobApplication.objects.all()
    wikiArticles = wikiArticle.objects.all()
    blogArticles = blogArticle.objects.all()
    ctx = {
        "transactions": transactions,
        "jobApplications": jobApplications,
        "wikiArticles": wikiArticles,
        "blogArticles": blogArticles,
    }
    return render (
        request,
        "homepage/dashboard.html",
        ctx
    )