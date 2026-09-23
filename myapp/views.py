from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Transaction
from .serializers import TransactionSerializer


@login_required
def index(request):
    """Render the main transaction dashboard."""
    return render(request, 'myapp/index.html')


class TransactionListCreate(generics.ListCreateAPIView):
    """List all transactions or create a new one."""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a single transaction."""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class LoginView(APIView):
    """Authenticate a user and return an API token."""

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_400_BAD_REQUEST
        )
