from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class HomeOwnerProfile(Profile):

    def __str__(self):
        return f"Homeowner profile for {self.user}"


class JobCategory(models.TextChoices):
    RENOVATION = 'renovation', 'Renovation'
    MAINTENANCE = 'maintenance', 'Maintenance'
    LANDSCAPING = 'landscaping', 'Landscaping'
    ELECTRICAL = 'electrical', 'Electrical'
    PLUMBING = 'plumbing', 'Plumbing'
    CLEANING = 'cleaning', 'Cleaning'
    OTHER = 'other', 'Other'


class ContractorProfile(Profile):
    available_status = models.BooleanField(
        default=True,
    )

    job_categories = ArrayField(
        models.CharField(
            max_length=30,
            choices=JobCategory.choices,
        ),
        blank=True,
        default=JobCategory,
    )

    experience = models.SmallIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Contractor profile for {self.user}"
