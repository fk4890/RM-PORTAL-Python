from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

from .constants import AccountsFormConstants, AccountsValues
from . import validators


class UserManager(BaseUserManager):
    """
    username / password / hire_date / is_ta / role / is_active を扱う最小構成のユーザーマネージャ。
    """

    def _build_user(
        self,
        username: str,
        password: str,
        *,
        is_ta: bool = False,
        role: str = AccountsValues.ROLE_VIEWER,
        hire_date=None,
        is_active: bool = True,
    ):
        validators.validate_username_required(username)
        validators.validate_password(password)
        user = self.model(
            username=username,
            is_ta=is_ta,
            role=role,
            hire_date=hire_date,
            is_active=is_active,
        )
        user.set_password(password)
        return user

    def create_user(
        self,
        username: str,
        password: str,
        *,
        is_ta: bool = False,
        role: str = AccountsValues.ROLE_VIEWER,
        hire_date=None,
        is_active: bool = True,
    ):
        user = self._build_user(
            username=username,
            password=password,
            is_ta=is_ta,
            role=role,
            hire_date=hire_date,
            is_active=is_active,
        )
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: str,
        password: str,
        *,
        is_ta: bool = False,
        role: str = AccountsValues.ROLE_VIEWER,
        hire_date=None,
        is_active: bool = True,
    ):
        """
        管理サイトは使わない前提なので、superuser 権限は付与しない。
        """
        user = self._build_user(
            username=username,
            password=password,
            is_ta=is_ta,
            role=role,
            hire_date=hire_date,
            is_active=True,  # superuser 相当は常に有効化して作成
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, null=False, blank=False, unique=True)
    hire_date = models.DateField(null=False, blank=False)
    is_ta = models.BooleanField(default=False)
    role = models.CharField(
        max_length=2,
        choices=AccountsFormConstants.ROLE_CHOICES,
        default=AccountsValues.ROLE_VIEWER,
    )
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS: list[str] = []

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"

    # 権限系は使用しないため False 固定
    @property
    def is_superuser(self) -> bool:
        return False

    @property
    def is_staff(self) -> bool:
        return False

    def has_perm(self, perm, obj=None) -> bool:
        return False

    def has_module_perms(self, app_label) -> bool:
        return False


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
