from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.db import models


class Candidate(models.Model):
    INFORMATION_TECHNOLOGY = 'IT'
    HUMAN_RESOURCE = 'HR'
    FINANCE = 'F'

    DEPARTMENTS_CHOICES = (
        (INFORMATION_TECHNOLOGY, 'IT'),
        (HUMAN_RESOURCE, 'HR'),
        (FINANCE, 'Finance')
    )

    full_name = models.CharField(max_length=256, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    years_of_experience = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MaxValueValidator(30),
            MinValueValidator(0)
        ]
    )
    department = models.CharField(
        max_length=64,
        choices=DEPARTMENTS_CHOICES
    )
    resume = models.FileField(
        upload_to='candidates_resumes',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])],
        null=True,
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name