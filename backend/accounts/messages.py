"""Message constants for the accounts app."""

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

from common.messages import LENGTH_RANGE, REQUIRED
from .constants import AccountsFormConstants


class LoginMessages:
    # ログイン画面向けのテンプレートとフィールド情報
    TEMPLATES = {
        "REQUIRED": REQUIRED,
        "LENGTH_RANGE": LENGTH_RANGE,
        "SUCCESS_ADMIN": "ログイン成功。管理者ダッシュボードへ遷移します。",
        "SUCCESS_MEMBER": "ログイン成功。メンバーダッシュボードへ遷移します。",
        "INVALID_CREDENTIALS": "ユーザー名またはパスワードが違います。",
        "INACTIVE_ACCOUNT": "アカウントが無効化されています（管理者に連絡してください）。",
    }

    LABELS = {
        "username": "ユーザー名",
        "password": "パスワード",
    }

    @classmethod
    def _username_length(cls):
        User = get_user_model()
        field = User._meta.get_field("username")
        min_len = AccountsFormConstants.USERNAME_MIN_LENGTH
        for v in field.validators:
            if isinstance(v, MinLengthValidator):
                min_len = v.limit_value
                break
        max_len = field.max_length or AccountsFormConstants.USERNAME_MAX_LENGTH
        return {"min_len": min_len, "max_len": max_len}

    @classmethod
    def rules(cls):
        return {
            "username": cls._username_length(),
            "password": {
                "min_len": AccountsFormConstants.PASSWORD_MIN_LENGTH,
                "max_len": AccountsFormConstants.PASSWORD_MAX_LENGTH,
            },
        }


__all__ = ["LoginMessages"]
