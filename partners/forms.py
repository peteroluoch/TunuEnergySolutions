from django import forms
from .models import Partner

class PartnerApplicationForm(forms.ModelForm):
    """
    Form for partner applications.
    """
    class Meta:
        model = Partner
        fields = [
            'name', 
            'email', 
            'phone', 
            'organization', 
            'website', 
            'partner_type', 
            'country', 
            'message'
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
