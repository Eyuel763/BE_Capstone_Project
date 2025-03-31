from rest_framework import serializers
from .models import Budget
    
class BudgetSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    wallet_name = serializers.CharField(source='wallet.name', read_only=True)
    
    class Meta:
        model = Budget
        fields = ('id', 'amount', 'category', 'category_name', 'wallet', 'wallet_name', 'month')
        read_only_fields = ('id',)
    
        def validate(self, data):
            if data['amount'] <= 0:
                raise serializers.ValidationError("Budget amount must be greater than zero.")
            return data