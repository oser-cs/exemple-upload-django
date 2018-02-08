from rest_framework import serializers
from upload.models import StudentRegistration
from .validators import FileValidator


class StudentRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentRegistration
        fields = ('id', 'first_name', 'last_name', 'image_agreement',
                  'submission_date',)
        extra_kwargs = {
            'image_agreement': {
                'validators': [
                    FileValidator(allowed_mimetypes=('application/pdf',)),
                ],
            },
            'submission_date': {
                'format': '%Y-%m-%d',
            }
        }
