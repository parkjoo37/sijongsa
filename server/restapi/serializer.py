from rest_framework import serializers
from .models import Member
from django.contrib.auth import get_user_model

# Serializers define the API representation.
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'name', 'age', 'email', 'password', 'gender', 'address', 'create_date', 'published_date']
