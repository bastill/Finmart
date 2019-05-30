from django.urls import path
from django.contrib.auth.views import (
    LoginView,LogoutView,PasswordChangeView,
    PasswordChangeDoneView,PasswordResetView,
    PasswordResetDoneView,PasswordResetCompleteView,
    PasswordResetConfirmView,
)

app_name = 'account'

urlpatterns = [
    path('auth/sign-in/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('auth/logout/', LogoutView.as_view(template_name='', name='logout')),
    path('auth/password-change/', PasswordChangeView.as_view(template_name=''), name='password'),
    path('auth/password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('auth/password-reset/', PasswordResetView.as_view(template_name=''), name='password-reset'),
    path('auth/password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('auth/password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_confirm'),
]

