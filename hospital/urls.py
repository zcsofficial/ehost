from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Root URL for hospital app
    path('book-appointment/', views.book_appointment, name='book_appointment'),
]
