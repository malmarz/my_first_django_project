from django.urls import path
from .views import test_view, greet_view

urlpatterns = [
    path('test/', test_view),
    path('greet/<str:u>/', greet_view),
    path('greet/<str:u>/<int:a>/', greet_view),
    
]