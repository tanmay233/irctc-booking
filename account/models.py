from django.db import models
from django.db.models.fields import proxy
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone
import uuid

# User roles
ADMIN = 0
READER = 1
WRITER = 2

class BaseModel(models.Model):
    """BaseModel for every child model"""

    # Unique identifier for each instance
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    # Timestamp for when the instance was created
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp for when the instance was last modified
    modified_at = models.DateTimeField(auto_now=True)
    # Soft delete flag
    is_deleted = models.BooleanField(default=False)
    # Active status flag
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True  # This model will not be used to create any database table

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        # Normalize the email address
        user = self.model(
            email=self.normalize_email(email),
        )

        # Set the user's password
        user.set_password(password)
        # Save the user to the database
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        # Grant admin privileges
        user.is_admin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, BaseModel):
    """Custom user model extending AbstractBaseUser and BaseModel"""
    
    # User's email address
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # Optional username
    username = models.CharField(unique=True, max_length=64, null=True, blank=True)
    # Optional name
    name = models.CharField(max_length=64, null=True, blank=True)
    
    # Phone number validation
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True) 

    # Registration timestamp
    user_registered_on = models.DateTimeField(default=timezone.now, blank=True)

    # Active status flag
    is_active = models.BooleanField(default=True)
    # Admin status flag
    is_admin = models.BooleanField(default=False)

    # Use AccountManager to manage user creation
    objects = AccountManager()

    # Use email as the unique identifier for authentication
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class AdminSecret(BaseModel):
    """Model to store encrypted API key secret for admin user"""
    # Link to the Account model
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    # API key for the admin user
    api_key = models.CharField(max_length=1000)
