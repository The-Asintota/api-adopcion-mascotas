from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)
import uuid


class CustomUserManager(UserManager):
    def _create_user(
        self,
        uuid=None,
        email=None,
        password=None,
        is_active=None,
        is_staff=None,
        is_superuser=None,
        last_login=None,
        date_joined=None,
    ):
        user = self.model(
            email=self.normalize_email(email),
            uuid=uuid,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=last_login,
            date_joined=date_joined,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        uuid=None,
        email=None,
        password=None,
        last_login=None,
        date_joined=None,
        **extra_fields,
    ):
        """
        Create and save a User with the given email and password.
        """

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)

        return self._create_user(
            email=email,
            uuid=uuid,
            password=password,
            last_login=last_login,
            date_joined=date_joined,
            **extra_fields,
        )

    def create_superuser(
        self,
        uuid=None,
        email=None,
        password=None,
        last_login=None,
        date_joined=None,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            email=email,
            uuid=uuid,
            password=password,
            last_login=last_login,
            date_joined=date_joined,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        db_column="uuid", primary_key=True, default=uuid.uuid4
    )
    email = models.EmailField(
        db_column="email",
        max_length=90,
        unique=True,
        blank=False,
        null=False,
    )
    password = models.CharField(
        db_column="password", max_length=128, blank=False, null=False
    )
    is_active = models.BooleanField(db_column="is active", default=False)
    is_staff = models.BooleanField(
        db_column="is_staff", default=False, serialize=False, db_index=True
    )
    is_superuser = models.BooleanField(
        db_column="is_superuser", default=False, serialize=False, db_index=True
    )
    last_login = models.DateTimeField(
        db_column="last login", blank=True, null=True
    )
    date_joined = models.DateTimeField(
        db_column="date joined", auto_now_add=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["is_active", "-date_joined"]
        indexes = [
            models.Index(
                fields=["email", "is_active"], name="email_is_active_idx"
            )
        ]

    def __str__(self):
        return self.email


class Shelter(models.Model):
    uuid = models.UUIDField(
        db_column="uuid", primary_key=True, default=uuid.uuid4
    )
    user = models.OneToOneField(
        to="User", to_field="uuid", db_column="user", on_delete=models.CASCADE
    )
    name = models.CharField(
        db_column="name", max_length=50, blank=False, null=False
    )
    address = models.CharField(
        db_column="address", max_length=100, blank=False, null=False
    )
    phone_number = models.CharField(
        db_column="phone_number", max_length=25, blank=False, null=False
    )
    responsible = models.CharField(
        db_column="responsible", max_length=50, blank=False, null=False
    )
    logo_url = models.URLField(
        db_column="logo_url", max_length=200, blank=False, null=False
    )
    data_joined = models.DateTimeField(
        db_column="date joined", auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shelters"
        verbose_name = "Shelter"
        verbose_name_plural = "Shelters"
        ordering = ["-data_joined"]
