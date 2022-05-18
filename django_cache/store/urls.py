# store/urls.py
from django.urls import path
from .views import view_books, view_cached_books
 
 
urlpatterns = [
    path('', view_books),
    path('cache/', view_cached_books),
]