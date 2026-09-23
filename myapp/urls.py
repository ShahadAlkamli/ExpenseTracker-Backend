from django.urls import path, include
from django.contrib.auth import views as auth_views

from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/transactions/', views.TransactionListCreate.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
