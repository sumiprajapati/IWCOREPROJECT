from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a user with the given email and password
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

class UserDetail(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', null=True, default="No image uploaded",blank=True)
    contact = models.CharField(null=True, blank=True, max_length=220)
    location = models.CharField(null=True, blank=True, max_length=250)
    position = models.CharField(null=True, blank=True, max_length=250)
    work = models.CharField(null=True, blank=True, max_length=250)
    cv = models.FileField(upload_to='cv/', null=True, default="No image uploaded", blank=True)

    def __str__(self):
        return '%s: %s' % ('Email',self.user.email)

class Partner(models.Model):
    partner_name = models.CharField(max_length=250,null=True,blank=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    detail = models.CharField(null=True,blank=True,max_length=250)
    project_file = models.FileField(upload_to='file/', null=True, default="No image uploaded", blank=True)

    def __str__(self):
        return '%s: %s' % ('Partner Name', self.partner_name)



class ProjectManager(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)


    def __str__(self):
        return '%s: %s' % ('ProjectManger Email', self.user.email)



class Developer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)


    def __str__(self):
        return '%s: %s' % ('Developer Email', self.user.email)



class Project(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, blank=True)
    project_manager = models.ForeignKey(ProjectManager, on_delete=models.CASCADE)
    developer = models.ManyToManyField(Developer, related_name='developers')
    project_name = models.CharField(null=True, blank=True, max_length=250)
    theme = models.CharField(null=True, blank=True, max_length=250)
    CHOICES = (
        ('ONGOING', 'ongoing'),
        ('COMPLETED', 'completed'),
        ('SUSPENDED', 'suspended'),
        ('QUEUED', 'queued'),
    )
    status = models.CharField(
        max_length=39,
        choices=CHOICES,
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '%s: %s' % ('Project Name', self.project_name)

