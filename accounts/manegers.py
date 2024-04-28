from  django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,phone_number,email,full_name,password=None):
        if not phone_number:
            raise ValueError('Phone number must be set')

        if not email:raise ValueError('email must be set')

        user = self.model(phone_number=phone_number,email=email,full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def creat_superuser(self,phone_number,email,full_name,password=None):
        user = self.create_user(phone_number,email,full_name,password)
        user.is_admin=True
        user.is_staff = True
        user.save(using=self._db)
        return user
