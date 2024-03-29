from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime

class BaseAbstractModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseAbstractModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        category = Category.objects.get(name='Developer') # fetch the default category
        extra_fields.setdefault('category', category)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    MALE = 'M'
    FEMALE = 'F'
    
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    
    STATUS_CHOICES = (
        ('M', 'Married'),
        ('S', 'Single'),
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    identity_number = models.CharField(null=True, blank=True, max_length=11)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=30, null=True)
    photo = models.ImageField(upload_to='profile', null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    marial_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'gender', 'birth_date', 'address', 'password', 'longitude', 'latitude', 'marial_status']

    def __str__(self):
        return f'{self.name} | {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
class Video(BaseAbstractModel):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} | {self.url}"

class City(BaseAbstractModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    def __str__(self):
        return self.name

class Discrict(BaseAbstractModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.name} | {self.city}'

class Hospital(BaseAbstractModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    discrict = models.ForeignKey(Discrict, on_delete=models.SET_NULL, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=13, null=True)
    latitude = models.DecimalField(max_digits=16, decimal_places=13, null=True)
    
    def __str__(self):
        return self.name

class Content(BaseAbstractModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    file = models.FileField(upload_to='documents', null=True)
    
    def __str__(self):
        return self.title

class Notification(BaseAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    
    def __str__(self):
        return f'{self.title} | {self.user.name}'

class Appointment(BaseAbstractModel):
    visitor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visitor', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visited')
    date_created = models.DateTimeField(auto_now_add=True)
    location = models.TextField()
    
    def __str__(self):
        return f'{self.user.name} | {self.datetime}'