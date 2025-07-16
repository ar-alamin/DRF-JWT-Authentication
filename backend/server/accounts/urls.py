from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('verify-email/', views.VerifyUserEmail.as_view(), name='verify'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('profile/', views.TestAuthenticationView.as_view(), name='granted'),
]
