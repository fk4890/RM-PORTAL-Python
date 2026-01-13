from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MEMBER = "MEMBER", "Member"

    hire_date = models.DateField(null=True, blank=True)
    is_ta = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"


class UserPlanSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="plan_settings")
    start_date = models.DateField(null=True, blank=True)
    target_months = models.PositiveSmallIntegerField(null=True, blank=True)
    daily_study_minutes = models.PositiveIntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"PlanSettings for {self.user.username}"


class UserPlanSettingsHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="plan_settings_history")
    applied_at = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(null=True, blank=True)
    target_months = models.PositiveSmallIntegerField(null=True, blank=True)
    daily_study_minutes = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["-applied_at"]

    def __str__(self) -> str:
        return f"History for {self.user.username} at {self.applied_at:%Y-%m-%d %H:%M}"

# Create your models here.
