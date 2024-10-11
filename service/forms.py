# service/forms.py
from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']

# service/forms.py
class ServiceRequestSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
    status = forms.ChoiceField(choices=[('all', 'All'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], required=False)
