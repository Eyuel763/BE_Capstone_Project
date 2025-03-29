from django.db import models
from django.conf import settings

class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallets')
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50) # e.g. "Checking", "Saving", "Credit Card"
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                name='balance_gte_0',
                check=models.Q(balance__gte=0)
            )
        ]

