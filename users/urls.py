from django.urls import path, include
from .views import home, profile, RegisterView
from . import views 
urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('com/', views.com, name="community"),
]
