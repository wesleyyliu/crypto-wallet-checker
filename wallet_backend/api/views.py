from django.shortcuts import render
from rest_framework import generics
from .serializers import WalletSerializer
from .models import Wallet

# Create your views here.
class WalletView(generics.CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    