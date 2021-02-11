from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from PIL import Image


# ****** Custom UserManager Model ******
class UserManager(BaseUserManager):

    # Creating user
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            return ValueError('User must have a email address.')
        if not password:
            return ValueError('User must have a password.')

        email = self.normalize_email(email)
        user_obj = self.model(email=email)
        user_obj.set_password(password)

        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin

        user_obj.save(using=self._db)
        return user_obj

    # Creating staff
    def create_staff(self,  email, password=None):
        user = self.create_user(
            email=email, password=password, is_staff=True,
        )
        return user

    # Creating superuser
    def create_superuser(self,  email, password=None):
        user = self.create_user(
            email=email, password=password, is_staff=True, is_admin=True,
        )
        return user


# ****** Custom User Model ******
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


# ****** User Profile Model ******
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True,
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics')
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{user.first_name} {user.last_name}'

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        # Resizing the image for better performance
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
