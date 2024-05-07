from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm, JobUpdateForm


# Create your views here.
class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions/commissions_list.html'
    context_object_name = 'commissions'

class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'commissions/commissions_detail.html'
    form_class = JobApplicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commission = self.get_object()
        jobs = commission.jobs.all()
        
        total_manpower_required = sum(job.people_required for job in jobs)
        total_signees = sum(job.applicant.count() for job in jobs)
        approved_signees = sum(job.applicant.filter(status='A').count() for job in commission.jobs.all())
        open_manpower = total_manpower_required - approved_signees
        
        context['form'] = self.form_class
        context['total_manpower_required'] = total_manpower_required
        context['open_manpower'] = open_manpower
        context['approved_signees'] = approved_signees
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            commission = self.get_object()
            application = form.save(commit=False)
            application.applicant = request.user.profile
            success_url = reverse_lazy('commissions:commission-list')

            jobs = commission.jobs.all()
            total_manpower_required = sum(job.people_required for job in jobs)
            total_signees = sum(job.applicant.count() for job in jobs)
            approved_signees = sum(job.applicant.filter(status='A').count() for job in commission.jobs.all())
            open_manpower = total_manpower_required - approved_signees

            if total_signees < total_manpower_required:
                application.status = 'P'
                application.save()
            elif open_manpower == 0:
                commission.status = 'F'
                commission.save()
                application.applicant_profile = self.request.user.profile
                application.save()
        return HttpResponseRedirect(reverse('commissions:commission-list'))
    def form_valid(self, form):
        commission = self.get_object()
        job = form.instance
        
        if all(application.status == 'A' for job in commission.jobs.all() for application in job.applicant.all()):
            job.status = 'F'  # Update job status to 'Full'
            job.save()
        
        if all(job.status == 'F' for job in commission.jobs.all()):
            commission.status = 'F'
            commission.save()
        
        return super().form_valid(form)

class CommissionUpdateView(UpdateView):
    model = Commission
    form_class = JobUpdateForm
    template_name = 'commissions/commissions_update.html'
    success_url = reverse_lazy('commissions:commission-list')
    
class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commissions_create.html'
    success_url = reverse_lazy('commissions:commission-list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            commission = form.save(commit=False)
            commission.owner = self.request.user.profile  
            commission.save()

            job_form = JobForm(self.request.POST, prefix='job')
            if job_form.is_valid():
                job = job_form.save(commit=False)
                job.commission = commission
                job.save()

            return redirect(self.success_url)
 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['commission_form'] = CommissionForm(self.request.POST)
            context['job_form'] = JobForm(self.request.POST, prefix='job')
        else:
            context['commission_form'] = CommissionForm()
            context['job_form'] = JobForm(prefix='job')
        return context