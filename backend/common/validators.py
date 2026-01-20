from django.core.exceptions import ValidationError

from . import messages


def validate_required(value, field_label: str) -> None:
    """
    共通の必須チェック。
    """
    if not value:
        raise ValidationError(messages.REQUIRED, code="required", params={"field": field_label})
