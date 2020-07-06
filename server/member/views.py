from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializer import MemberSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.contrib.auth.hashers import check_password

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        print(self.request.POST['email'])
        print(self.request.POST['password'])

        qs = self.queryset.filter(email=self.request.POST['email'])
        print(qs)
        serializer = self.get_serializer(qs, many=True)

        # for i in serializer.data:
        #     print(i)
        #
        # print(serializer.data[0])
        return Response(serializer.data)


        # user.check_password(request.password)
        # email = self.queryset.filter(email=request.email)
        # password = self.queryset.filter(password=request.password)
        #
        # if email is not None and password is not None:
        #     serializer = self.get_serializer(email)
        #
        # print(serializer.data)
        #
        # return Response(serializer.data)
