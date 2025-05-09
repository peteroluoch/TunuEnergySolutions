from django.db import models
from django.utils.translation import gettext_lazy as _

class Partner(models.Model):
    """
    Model for partners.
    """
    PARTNER_TYPES = (
        ('distributor', 'Distributor'),
        ('ngo', 'NGO'),
        ('government', 'Government'),
        ('research', 'Research Institution'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    organization = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPES)
    country = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.get_partner_type_display()})"
