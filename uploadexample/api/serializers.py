from rest_framework import serializers
from upload.models import StudentRegistration


class StudentRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentRegistration
        fields = ('id', 'first_name', 'last_name', 'image_agreement',
                  'submission_date',)
        extra_kwargs = {
            'submission_date': {
                'format': '%Y-%m-%d',
            }
        }
