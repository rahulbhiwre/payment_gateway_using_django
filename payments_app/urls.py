from django.urls import path
from .views import initiate_payment, callback ,UserRegisterView

urlpatterns = [
    path('pay/', initiate_payment, name='pay'),
    path('callback/', callback, name='callback'),
    path('',UserRegisterView.as_view(),name='register'),
]