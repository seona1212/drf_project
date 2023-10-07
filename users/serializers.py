from rest_framework import serializers
from users.models import User


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        print(validated_data)
        password = user.password
        user.set_passwrd(password)
        print(user.passwrd)
        return user