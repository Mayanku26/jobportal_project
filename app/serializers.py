from rest_framework import serializers
from .models import singup


class signupserializer(serializers.ModelSerializer):
    class Meta:
        model = singup
        fields = ["id", "email"]
