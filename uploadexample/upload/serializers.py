from rest_framework import serializers
from .models import StudentRegistration
from .validators import FileValidator


class StudentRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentRegistration
        fields = ('first_name', 'last_name', 'image_agreement')
        extra_kwargs = {
            'image_agreement': {
                'validators': [
                    FileValidator(allowed_mimetypes=('application/pdf',)),
                ],
            }
        }
