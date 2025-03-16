from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =('id', 'email', 'first_name', 'last_name','password', 'is_staff', 'is_active', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            print(f"Password before hashing: {validated_data['password']}")
            user = CustomUser.objects.create_user(**validated_data)
            user.set_password(validated_data['password'])
            print(f"Password after hashing: {user.password}")
            user.save()
            return user