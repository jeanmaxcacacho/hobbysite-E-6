from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Commission, Job

# Create your views here.
class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions/commissions_list.html'
    context_object_name = 'commission'

class CommissionDetailView(DetailView):
    model = Job
    template_name = 'commissions/commissions_detail.html'
    context_object_name = 'commission'
