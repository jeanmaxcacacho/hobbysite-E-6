from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from merchstore.models import ProductType, Product, Transaction
from wiki.models import Article

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
"""
@login_required
def dashboard(request):
    transactions = Transaction.objects.all()
    wiki_articles = Article.objects.all()

    ctx = {

    }
    return render (
        request,
        "homepage/dashboard.html",
        ctx
    )