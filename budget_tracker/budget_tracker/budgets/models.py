from django.db import models
from django.conf import settings
from wallets.models import Wallet
from transactions.models import Category

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='budgets')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budgets')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='budgets', blank=True, null=True)  # Optional
    month = models.DateField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='budget_amount_gt_0',
                check=models.Q(amount__gt=0)
            ),
            models.UniqueConstraint(
                fields=['user', 'category', 'month'],
                name='unique_budget_per_category_month'
            )
        ]

    def __str__(self):
        return f"Budget of {self.amount} for {self.category} in {self.month.strftime('%B %Y')}"

