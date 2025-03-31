from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
    
router = DefaultRouter()
router.register(r'budgets', views.BudgetViewSet, basename='budget')
    
urlpatterns = [
    path('', include(router.urls)),
]