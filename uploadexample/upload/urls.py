from django.urls import path
from .views import RegistrationCreate, RegistrationList, RegistrationDelete


urlpatterns = [
    path('', RegistrationList.as_view(), name='registration-list'),
    path('inscription', RegistrationCreate.as_view(),
         name='registration-create'),
    path('inscription/<int:pk>', RegistrationDelete.as_view(),
         name='registration-delete'),
]
