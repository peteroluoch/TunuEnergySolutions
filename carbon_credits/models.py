from django.db import models
from django.contrib.auth.models import User

class CarbonCredit(models.Model):
    """
    Model for carbon credits.
    """
    credit_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount in tons of CO2 equivalent")
    price_per_ton = models.DecimalField(max_digits=10, decimal_places=2)
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    verification_standard = models.CharField(max_length=100, help_text="e.g., Gold Standard, VCS")
    verification_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.credit_id} - {self.amount} tons"

    @property
    def total_price(self):
        return self.amount * self.price_per_ton

class CarbonCreditTransaction(models.Model):
    """
    Model for carbon credit transactions.
    """
    TRANSACTION_TYPES = (
        ('purchase', 'Purchase'),
        ('sale', 'Sale'),
        ('retirement', 'Retirement'),
    )

    carbon_credit = models.ForeignKey(CarbonCredit, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_ton = models.DecimalField(max_digits=10, decimal_places=2)
    buyer = models.ForeignKey(User, related_name='credit_purchases', on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(User, related_name='credit_sales', on_delete=models.CASCADE, null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} tons from {self.carbon_credit.credit_id}"

    @property
    def total_price(self):
        return self.amount * self.price_per_ton
