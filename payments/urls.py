from django.urls import path
from .views import *

urlpatterns = [
    path('', product_create, name='create'),
    path('edit/<id>/', product_edit, name='edit'),
    path('detail/<id>/', PaymentConfirmation.as_view(), name='detail'),
    path('success/', PaymentSuccessView, name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
    path('history/', OrderHistoryListView.as_view(), name='history'),
    path('api/checkout-session/<id>/', create_checkout_session, name='api_checkout_session'),
]