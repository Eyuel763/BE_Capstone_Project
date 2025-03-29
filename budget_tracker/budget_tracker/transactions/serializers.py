from rest_framework import serializers
from .models import Transaction, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)

class TransactionSerializer(serializers.ModelSerializer):
        category = CategorySerializer(read_only=True)
        category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, source='category')
        
        class Meta:
            model = Transaction
            fields = ('id', 'amount', 'type', 'category', 'category_id', 'wallet', 'date', 'description')
            read_only_fields = ('id',)
    
        def validate(self, data):
            if data['type'] not in ('income', 'expense'):
                raise serializers.ValidationError("Transaction type must be either 'income' or 'expense'.")
            return data