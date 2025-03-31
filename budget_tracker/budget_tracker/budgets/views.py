from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Budget
from .serializers import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['month', 'amount']
    
    def get_queryset(self):
        queryset = Budget.objects.filter(user=self.request.user)
        category_id = self.request.query_params.get('category_id')
        wallet_id = self.request.query_params.get('wallet_id')
        month = self.request.query_params.get('month')
    
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if wallet_id:
            queryset = queryset.filter(wallet_id=wallet_id)
        if month:
            queryset = queryset.filter(month=month)
    
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['GET'])
    def details(self, request, pk=None):
        """
        Additional details about a budget (if needed).
        """
        budget = self.get_object()
        serializer = self.get_serializer(budget)
        return Response(serializer.data)
