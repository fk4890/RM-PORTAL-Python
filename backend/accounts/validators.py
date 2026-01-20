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
