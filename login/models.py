from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, uid, username, password=None):

        if not uid:
            raise ValueError('must have user uid')
        if not username:
            raise ValueError('must have user username')

        user = self.model(
            uid=uid,
            username=username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, uid, username, password=None):

        user = self.create_user(
            uid=uid,
            username = username,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin,TimeStampMixin):

    objects = UserManager()

    uid = models.PositiveBigIntegerField(unique=True, null = True, default=0)
    username = models.CharField(max_length=10)
    exp = models.DateTimeField(default=timezone.now)
    refresh = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    indexes = [
        models.Index(fields=['id'])
    ]

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.uid) + ' ' + self.username

    @property
    def is_staff(self):
        return self.is_admin
    


