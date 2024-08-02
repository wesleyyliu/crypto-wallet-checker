from django.urls import path
from .views import WalletView

urlpatterns = [
    path('wallets', WalletView.as_view())
]
