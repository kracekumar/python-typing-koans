from rest_framework import serializers
from typing import Optional, TypedDict
from datetime import datetime


class Comment:
    def __init__(self, email: str, content: str, created: Optional[datetime] = None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data) -> Comment:
        return Comment(**validated_data)

    def update(self, instance: Comment, validated_data) -> Comment:
        instance.email = validated_data.get("email", instance.email)
        instance.content = validated_data.get("content", instance.content)
        instance.created = validated_data.get("created", instance.created)
        return instance
