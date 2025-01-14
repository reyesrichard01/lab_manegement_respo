from rest_framework import generics
from .models import Lab
from .serializers import LabSerializer

class LabListCreateView(generics.ListCreateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class LabDetailView(generics.RetrieveAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
