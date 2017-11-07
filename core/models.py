from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
from django.urls import reverse

class UserManager(BaseUserManager):
    def create_user(self, email, first_name,last_name, phone_number, password=None):
        """
        Creates and saves a User with the given email and password.
        REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number', 'password']
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name,last_name, phone_number, password):
        """
    Not implemented yet - 05/Nov/207
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email, first_name,last_name, phone_number,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,last_name, phone_number, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email, first_name,last_name, phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # Create a new class that overrides Django's base user class
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    last_name = models.CharField(max_length=25, blank=True )
    first_name = models.CharField(max_length=25, blank=True )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    role = models.ForeignKey('Roles', on_delete=models.SET_NULL, null=True)
    created_date = models.DateField(auto_now_add=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name', 'phone_number'] # Email & Password are required by default.

    class Meta:
        ordering = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('core:user-detail', args=[str(self.id)])

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Roles(models.Model):
    # TODO: roles to be added
    pass