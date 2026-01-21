from django.core.exceptions import ValidationError

from common import messages as common_messages
from common import validators as common_validators

from .constants import AccountsFormConstants as AFC, AccountsLabel as AL


def validate_username_required(value: str) -> None:
    common_validators.validate_required(value, AL.USERNAME_LABEL)


def validate_password(value: str) -> None:
    common_validators.validate_required(value, AL.PASSWORD_LABEL)
    length = len(value)
    if length < AFC.PASSWORD_MIN_LENGTH or length > AFC.PASSWORD_MAX_LENGTH:
        raise ValidationError(
            common_messages.LENGTH_RANGE,
            code="invalid_length",
            params={
                "field": AL.PASSWORD_LABEL,
                "min_len": AFC.PASSWORD_MIN_LENGTH,
            "max_len": AFC.PASSWORD_MAX_LENGTH,
        },
    )


def validate_daily_study_minutes(value: int) -> None:
    """
    1日あたりの学習時間（分）に上限を設定（デフォルト 1440 分）。
    """
    if value is None:
        return
    if value > AFC.DAILY_STUDY_MINUTES_MAX:
        raise ValidationError(
            common_messages.LENGTH_RANGE,
            code="invalid_length",
            params={
                "field": "1日学習時間(分)",
                "min_len": 1,
                "max_len": AFC.DAILY_STUDY_MINUTES_MAX,
            },
        )
