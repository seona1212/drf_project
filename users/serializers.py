from rest_framework import serializers
from users.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.email
        # ...

        return token