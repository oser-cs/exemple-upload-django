from rest_framework import viewsets
from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin, ListModelMixin)
from upload.models import StudentRegistration
from .serializers import StudentRegistrationSerializer


class RegistrationViewSet(ListModelMixin,
                          CreateModelMixin,
                          DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = StudentRegistration.objects.all()
    serializer_class = StudentRegistrationSerializer
