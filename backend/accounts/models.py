from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    username / password / hire_date / is_ta / role / is_active だけを持つ最小構成のユーザーマネージャ。
    Django標準のパスワードハッシュを利用する。
    """

    def create_user(self, username: str, password: str | None = None, **extra_fields):
        if not username:
            raise ValueError("username is required")
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username: str, password: str, **extra_fields):
        """
        管理サイトは使わない前提なので、superuser 権限は持たせずに作成。
        """
        extra_fields.setdefault("is_active", True)
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = "00", "管理者"
        GL = "01", "GL"
        TL = "02", "TL"
        MEMBER = "03", "メンバー"
        VIEWER = "05", "参照"

    username = models.CharField(max_length=150, unique=True)
    hire_date = models.DateField(null=True, blank=True)
    is_ta = models.BooleanField(default=False)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.VIEWER)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS: list[str] = []

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"

    # 権限系は今回の要件では使用しないため False 固定
    @property
    def is_superuser(self) -> bool:  # django.contrib.auth.backends.ModelBackend が参照するためプロパティを提供
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

# Create your models here.
