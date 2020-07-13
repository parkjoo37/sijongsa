from rest_framework import serializers
from .models import Member
from rest_auth.registration.serializers import RegisterSerializer

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class MemberRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required = True)
    age = serializers.IntegerField(required = True)
    gender = serializers.IntegerField(required = True)
    address = serializers.CharField(required = True)

    def get_cleaned_data(self):
        # data_dict = super().get_cleaned_data()
        # data_dict['username'] = self.validated_data.get('username', '')
        # data_dict['age'] = self.validated_data.get('age', '')
        # data_dict['gender'] = self.validated_data.get('gender', '')
        # data_dict['address'] = self.validated_data.get('address', '')

        # return data_dict
        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'username': self.validated_data.get('username', ''),
            'age': self.validated_data.get('age', ''),
            'gender': self.validated_data.get('gender', ''),
            'address': self.validated_data.get('address', '')
        }
