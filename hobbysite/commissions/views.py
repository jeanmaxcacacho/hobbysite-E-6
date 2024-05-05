from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Commission
from .forms import CommissionForm, JobForm, JobApplicationForm


# Create your views here.
class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions/commissions_list.html'
    context_object_name = 'commissions'
    

class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'commissions/commissions_detail.html'

class CommissionUpdateView(UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commissions_update.html'
    success_url = reverse_lazy('commissions:commission-list')

  
class CommissionCreateView(CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commissions_create.html'
    success_url = reverse_lazy('commissions:commission-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['commission_form'] = CommissionForm(self.request.POST)
            context['job_form'] = JobForm(self.request.POST, prefix='job')
            context['job_application_form'] = JobApplicationForm(self.request.POST, prefix='job_application')
        else:
            context['commission_form'] = CommissionForm()
            context['job_form'] = JobForm(prefix='job')
            context['job_application_form'] = JobApplicationForm(prefix='job_application')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        commission_form = context['commission_form']
        job_form = context['job_form']
        job_application_form = context['job_application_form']
        if (commission_form.is_valid() and job_form.is_valid() and job_application_form.is_valid()):
            commission = commission_form.save()
            job = job_form.save(commit=False)
            job.commission = commission
            job.save()
            job_application = job_application_form.save(commit=False)
            job_application.job = job
            job_application.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
