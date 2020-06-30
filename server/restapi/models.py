from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50, verbose_name='이름', null=False)
    age = models.IntegerField(verbose_name='나이', null=False)
    email = models.EmailField(max_length=100, verbose_name='이메일', null=False)
    password = models.CharField(max_length=100, verbose_name='비밀번호', null=False)
    gender = models.IntegerField(verbose_name='성별', null=False)
    address = models.TextField(max_length=200, verbose_name='주소', null=False)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')
    published_date = models.DateTimeField(blank=True, verbose_name='수정날짜', null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
