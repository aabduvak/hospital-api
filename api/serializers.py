from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import User, Group

class UserSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]
    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')
        extra_kwargs = {'password': {'write_only': True}}
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # Call the parent class's update() method to update the other fields
        instance = super().update(instance, validated_data)

        # If the password field is present in the request, encrypt it and save it to the instance
        if password is not None:
            instance.set_password(password)
            instance.save()
        
        return instance