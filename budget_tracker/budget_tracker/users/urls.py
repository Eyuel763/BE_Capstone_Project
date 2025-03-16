from django.urls import path
from .views import UserCreateView, LoginView, home
from django.contrib.auth.views import LoginView, LogoutView
#from .views import RegisterView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    #path('login/', LoginView.as_view(), name='user-login',)
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('register/', RegisterView.as_view(), name='register'),
]