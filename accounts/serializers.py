from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'links']

    def get_links(self, obj):
        request = self.context.get('request')
        if not request:
            return []
            
        return [
            {
                "rel": "self",
                "href": reverse('me', request=request),
                "method": "GET"
            }
        ]
