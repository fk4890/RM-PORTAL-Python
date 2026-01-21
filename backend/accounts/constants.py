"""
accounts アプリで使う定数置き場。
モデルやフォームのラベル / 値 / バリデーションをまとめて管理する。
"""


class AccountsLabel:
    """User モデルで使うラベル"""

    USERNAME_LABEL = "ユーザー名"
    PASSWORD_LABEL = "パスワード"
    HIRE_DATE_LABEL = "入社日"
    IS_TA_LABEL = "TAフラグ"
    ROLE_LABEL = "権限"
    IS_ACTIVE_LABEL = "有効フラグ"


class AccountsValues:
    """User モデルで使う値"""

    # ロール
    ROLE_ADMIN = "00"   # 管理者
    ROLE_GL = "01"      # GL
    ROLE_TL = "02"      # TL
    ROLE_MEMBER = "03"  # メンバー
    ROLE_VIEWER = "05"  # 参照


class AccountsFormConstants:
    """User 関連のバリデーション・選択肢"""

    USERNAME_MIN_LENGTH = 1
    USERNAME_MAX_LENGTH = 8
    PASSWORD_MIN_LENGTH = 4
    PASSWORD_MAX_LENGTH = 32
    DAILY_STUDY_MINUTES_MAX = 1440  # 24時間を上限にする

    ROLE_CHOICES = [
        (AccountsValues.ROLE_ADMIN, "管理者"),
        (AccountsValues.ROLE_GL, "GL"),
        (AccountsValues.ROLE_TL, "TL"),
        (AccountsValues.ROLE_MEMBER, "メンバー"),
        (AccountsValues.ROLE_VIEWER, "参照"),
    ]


class GeneralConstants:
    REQUIRED_LABEL = "必須"
    OPTIONAL_LABEL = "任意"
