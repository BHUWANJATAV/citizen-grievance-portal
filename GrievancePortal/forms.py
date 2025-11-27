from django import forms
from .models import Grievance

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance

        #important status ka option only admin ko,user ko nhi
        fields = ['title', 'category', 'location', 'description', 'evidence_image']
        