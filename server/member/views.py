from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializer import MemberSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.hashers import check_password

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        email = self.request.POST['email']
        password = self.request.POST['password']

        print(email)
        print(password)

        find_account = self.queryset.filter(email=email)
        old_password = find_account[0].password

        # print(find_account[0].url)

        if find_account is not None:
            if check_password(password, old_password):
                serializer = self.get_serializer(find_account, many=True)
                print(serializer.data[0]['url'])
                return Response({ 'url': serializer.data[0]['url'] })


        # oldPassword = self.queryset[0].password
        # print(check_password(self.request.POST['password'], oldPassword))

        # print(qs[0].password)

        # [print(i.password) for i in self.queryset]
        serializer = self.get_serializer(qs, many=True)

        # for i in serializer.data:
        #     print(i)
        #
        print(serializer.data[0])
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
