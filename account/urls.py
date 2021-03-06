from django.urls import path, include
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendResetPasswordEmailView, UserPasswordResetView, UserProfile

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('user-profile/', UserProfile.as_view(), name='users-profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('send-reset-password-email/', SendResetPasswordEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]
