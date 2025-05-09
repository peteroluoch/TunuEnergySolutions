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

    name = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    joined_on = models.DateTimeField(auto_now_add=True)
    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPES, default='other')
    website = models.URLField(blank=True)

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
        ordering = ['name']

    def __str__(self):
        return self.name
