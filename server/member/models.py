from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyMemberManager(BaseUserManager):
    def create_user(self, email, username, age, gender, address, password=None):
        if not email:
            raise ValueError("사용자는 메일주소가 있어야합니다.")
        if not username:
            raise ValueError("사용자는 이름이 있어야합니다.")
        if not age:
            raise ValueError("사용자는 나이가 있어야합니다.")
        if not gender:
            raise ValueError("사용자는 성별이 있어야합니다.")
        if not address:
            raise ValueError("사용자는 주소가 있어야합니다.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            age = age,
            gender = gender,
            address = address,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, age, gender, address, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            age = age,
            gender = gender,
            address = address,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# Create your models here.
class Member(AbstractBaseUser):
    email = models.EmailField(verbose_name="이메일", max_length=60, unique=True)
    username = models.CharField(verbose_name="이름", max_length=30, unique=True)
    age = models.IntegerField(verbose_name='나이', null=False)
    gender = models.IntegerField(verbose_name='성별', null=False)
    address = models.TextField(max_length=200, verbose_name='주소', null=False)
    date_joined = models.DateTimeField(verbose_name='가입일', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='최근로그인', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'age', 'gender', 'address',]

    objects = MyMemberManager()

    def __str__(self):
        return self.email

    def has_perms(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
