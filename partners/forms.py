from django import forms
from .models import Partner

class PartnerApplicationForm(forms.ModelForm):
    """
    Form for partner applications.
    """
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)

    class Meta:
        model = Partner
        fields = [
            'name',
            'contact_person',
            'email',
            'phone',
            'region',
            'partner_type',
            'website'
        ]
