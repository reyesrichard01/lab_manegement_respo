from django.urls import path
from .views import LabListCreateView, LabDetailView

urlpatterns = [
    path('labs/', LabListCreateView.as_view(), name='lab-list-create'),
    path('labs/<int:pk>/', LabDetailView.as_view(), name='lab-detail'),
]
