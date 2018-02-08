from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from . import views


urlpatterns = [
    path('docs', include_docs_urls(title='API'))
]

router = DefaultRouter()
router.register(r'registrations', views.RegistrationViewSet)
urlpatterns += router.urls
