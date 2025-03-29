from django.db import models
from django.conf import settings
from wallets.models import Wallet

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='catagories')
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=[('income', 'Income'), ('expense', 'Expense')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']
        constraints = [
            models.CheckConstraint(
                name='amount_gt_0',
                check=models.Q(amount__gt=0)
            )
        ]

    def __str__(self):
        return f"{self.type.capitalize()} of {self.amount} in {self.wallet.name} on {self.date}"

