from django.db import transaction
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'specialization', 'city']
    ordering = ['id']

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()

    def perform_update(self, serializer):
        with transaction.atomic():
            serializer.save()
