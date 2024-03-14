from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Commission, Comment

# Create your views here.
class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions/commissions_list.html'

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commissions/commissions_detail.html'
