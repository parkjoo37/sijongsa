from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializer import MemberSerializer, MemberRegisterSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_auth.registration.views import RegisterView

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    # @action(detail=False, methods=['post'])
    # def login(self, request):
    #     email = self.request.POST['email']
    #     password = self.request.POST['password']
    #
    #     print(email)
    #     print(password)
    #
    #     find_account = self.queryset.filter(email=email)
    #     old_password = find_account[0].password
    #
    #     if find_account is not None:
    #         if check_password(password, old_password):
    #             serializer = self.get_serializer(find_account, many=True)
    #             print(serializer.data[0]['url'])
    #             return Response({ 'url': serializer.data[0]['url'] })
    #         else:
    #             return Response({ 'url': 'fail' })
    #
    #     serializer = self.get_serializer(qs, many=True)
    #
    #     print(serializer.data[0])
    #     return Response(serializer.data)

class MemberRegisterViewSet(RegisterView):
    serializer_class = MemberRegisterSerializer
