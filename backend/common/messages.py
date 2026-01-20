"""
Shared message templates usable across apps.
差し込みは ValidationError(params=...) 前提。
"""

REQUIRED = "%(field)sは必須です"
LENGTH_RANGE = "%(field)sは%(min_len)s〜%(max_len)s文字で入力してください"
