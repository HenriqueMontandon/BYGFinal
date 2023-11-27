from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('empresa_signup/', views.empresa_signup, name='empresa_signup'),
]