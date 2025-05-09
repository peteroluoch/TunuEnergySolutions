from django.db import models
from django.urls import reverse

class InvestmentOpportunity(models.Model):
    """
    Model for investment opportunities.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    amount_needed = models.DecimalField(max_digits=12, decimal_places=2)
    minimum_investment = models.DecimalField(max_digits=10, decimal_places=2)
    expected_return = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    risk_level = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Investment Opportunities"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('investors:investment_detail', args=[self.slug])

class InvestorInquiry(models.Model):
    """
    Model for investor inquiries.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    opportunity = models.ForeignKey(InvestmentOpportunity, on_delete=models.SET_NULL, null=True, blank=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Investor Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry from {self.name}"
