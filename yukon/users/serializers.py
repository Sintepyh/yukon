from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, value):
        # Перевіряємо, чи користувач з таким ім'ям вже існує
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Користувач з таким іменем вже існує')
        return value

    def validate(self, data):
        # Перевіряємо, чи паролі співпадають
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError('Паролі не співпадають')
        return data

    def create(self, validated_data):
        # Створюємо користувача з серіалайзера
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password1'],
        )
        return user

