"""Regular Django views for a template-based frontend."""
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView

from .models import StudentRegistration

# Create your views here.


class RegistrationList(ListView):
    """List of the registrations."""

    model = StudentRegistration
    context_object_name = 'registrations'


class RegistrationCreate(CreateView):
    """Create a new registration."""

    model = StudentRegistration
    fields = ('first_name', 'last_name', 'image_agreement')
    success_url = reverse_lazy('registration-list')

    def get_form(self, **kwargs):
        """Customize style by adding Bootstrap classes."""
        form = super().get_form(**kwargs)
        classes = {
            'first_name': 'form-control',
            'last_name': 'form-control',
            'image_agreement': 'form-control-file',
        }
        for field in form.fields:
            form.fields[field].widget.attrs.update({'class': classes[field]})
        return form

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Inscription réussie')
        return response


class RegistrationDelete(DeleteView):
    """Delete a registration after confirmation."""

    model = StudentRegistration
    success_url = reverse_lazy('registration-list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Inscription supprimée')
        return response
