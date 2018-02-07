from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from .models import StudentRegistration
from .serializers import StudentRegistrationSerializer

# Create your views here.


class RegistrationCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload/registration_create.html'

    def get(self, request):
        registration = StudentRegistration()
        serializer = StudentRegistrationSerializer(registration)
        return Response({'serializer': serializer})

    def post(self, request):
        registration = StudentRegistration()
        serializer = StudentRegistrationSerializer(
            registration, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        messages.success(request, 'Inscription réussie')
        return redirect('registration-list')


class RegistrationList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload/registration_list.html'

    def get(self, request):
        queryset = StudentRegistration.objects.all()
        return Response({'registrations': queryset})


class RegistrationDelete(APIView):

    def get(self, request, pk):
        registration = get_object_or_404(StudentRegistration, pk=pk)
        registration.delete()
        messages.success(request, 'Inscription supprimée')
        return redirect('registration-list')
