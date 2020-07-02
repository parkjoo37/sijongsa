from rest_framework import serializers
from .models import Member

# Serializers define the API representation.
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['url', 'name', 'age', 'email', 'password', 'gender', 'address', 'create_date', 'published_date']
