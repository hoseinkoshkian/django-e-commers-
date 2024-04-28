from django.db import models
from  django.contrib.auth.models import AbstractUser , AbstractBaseUser
from .manegers import UserManager
class user(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    phone_number = models.CharField(max_length=11 ,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255)
    USERNAME_FIELD = 'phone_number' # فیلدی که کاربر با آن ثبت نام میشود و این فید حتما باید یونیکش ترو باشد 
    REQUIRED_FIELDS = ['email'] #فقط برای ساخت سوپر یوزر کاربرد دارد و پسورد و شماره تلفن را به صورت اجباری میپرسد
    objects = UserManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): #پرمیژن ها که جای دیگر تنظیم میکنیم و اینجا به همه اجازه میدهیم

        return  True

    def has_module_perms(self): #دسترسی به مدل های جنگو
        return True

    @property
    def is_staff(self): return self.is_admin


