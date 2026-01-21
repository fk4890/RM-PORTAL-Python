from rest_framework import serializers

from .messages import LoginMessages


class LoginMessagesSerializer(serializers.Serializer):
    templates = serializers.DictField(child=serializers.CharField(), read_only=True)
    labels = serializers.DictField(child=serializers.CharField(), read_only=True)
    rules = serializers.DictField(child=serializers.DictField(), read_only=True)

    def to_representation(self, instance):
        # instance は None を想定。定数をそのまま返す。
        return {
            "templates": LoginMessages.TEMPLATES,
            "labels": LoginMessages.LABELS,
            "rules": LoginMessages.rules(),
        }
