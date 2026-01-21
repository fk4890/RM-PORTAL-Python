from django.urls import path

from .views import LoginMessagesView, LoginView

app_name = "accounts"

urlpatterns = [
    path("login/messages", LoginMessagesView.as_view(), name="login-messages"),
    path("auth/login", LoginView.as_view(), name="auth-login"),
]
