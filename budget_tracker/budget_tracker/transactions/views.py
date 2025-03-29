from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
from wallets.models import Wallet
from django.db import transaction

class CategoryViewSet(viewsets.ModelViewSet):
        serializer_class = CategorySerializer
        permission_classes = [permissions.IsAuthenticated]
    
        def get_queryset(self):
            return Category.objects.filter(user=self.request.user)
    
        def perform_create(self, serializer):
            serializer.save(user=self.request.user)
    
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'amount']
    
    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        wallet_id = self.request.query_params.get('wallet_id')
        if wallet_id:
            queryset = queryset.filter(wallet_id=wallet_id)
        return queryset
    
    def perform_create(self, serializer):
        with transaction.atomic():  
            serializer.save(user=self.request.user)
            instance = serializer.instance  
            wallet = instance.wallet
            if instance.type == 'income':
                wallet.balance += instance.amount
            elif instance.type == 'expense':
                wallet.balance -= instance.amount
            wallet.save()

    def perform_destroy(self, instance):
        with transaction.atomic(): 
            wallet = instance.wallet
            amount = instance.amount
            type = instance.type

            instance.delete()

            if type == 'income':
                wallet.balance -= amount
            elif type == 'expense':
                wallet.balance += amount
            wallet.save()
    
    @action(detail=True, methods=['GET'])
    def details(self, request, pk=None):
        """
        Additional details about a transaction (if needed).
        """
        transaction = self.get_object()
        serializer = self.get_serializer(transaction)
        return Response(serializer.data)
