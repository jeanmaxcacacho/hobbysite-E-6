from django import forms 
from .models import Commission, JobApplication, Job
from django.forms import Textarea

class CommissionForm(forms.ModelForm):
    class Meta: 
        model = Commission
        fields = "__all__"

class JobForm(forms.ModelForm):
    class Meta: 
        model = Job
        fields = "__all__"
        widgets = {
            'role': Textarea(attrs={'cols': 18, 'rows': 1}),
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = "__all__"


