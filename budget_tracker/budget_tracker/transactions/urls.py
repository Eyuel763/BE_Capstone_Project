from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
    
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
    
urlpatterns = [
    path('', include(router.urls)),
]