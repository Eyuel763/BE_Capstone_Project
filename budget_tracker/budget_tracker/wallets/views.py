from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet
from .serializers import WalletSerializer

class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['PUT'])
    def update_balance(self, request, pk=None):
        try:
            wallet = self.get_object()
            new_balance = request.data.get('balance')
            if new_balance is not None:
                wallet.balance = new_balance
                wallet.save()
                serializer = self.get_serializer(wallet)
                return Response(serializer.data)
            else:
                return Response({'error': 'Balance is required. '}, status=status.HTTP_400_BAD_REQUEST)
        except Wallet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def perform_destroy(self, instance):
        # Check if there are any transactions associated with the wallet
        if not instance.transactions.exists():
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error' : 'Cannot delete wallet with associated transactions.'}, status=status.HTTP_400_BAD_REQUEST)

