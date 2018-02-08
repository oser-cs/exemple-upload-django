from django.db import models

# Create your models here.


class StudentRegistration(models.Model):
    """A simple model to represent a student registration application.

    Contains two regular char fields and a file field for the actual
    application file.
    """

    first_name = models.CharField('prénom', max_length=200)
    last_name = models.CharField('nom', max_length=200)
    submission_date = models.DateTimeField(auto_now_add=True)
    # Note that deleting a StudentRegistration object does NOT automatically
    # delete the associated file.
    # It must be deleted either manually or during a periodic cleanup
    # task (e.g. Cron job).
    # See here:
    # https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.fields.files.FieldFile.delete
    image_agreement = models.FileField("autorisation de droit à l'image")

    class Meta:  # noqa
        verbose_name = "dossier d'inscription"
        verbose_name_plural = "dossiers d'inscription"
        ordering = ('-submission_date',)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
