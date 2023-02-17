from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/books', views.apiBooks, name='api/books'),
    path('api/books/<int:id>', views.apiBooksId, name='api/books/id'),
]
