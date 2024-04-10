from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField
from uuid import uuid4, UUID


class CustomUserManager(UserManager):
    def _create_user(
        self,
        uuid: UUID = None,
        email: str = None,
        password: str = None,
        **extra_fields,
    ):
        user = self.model(
            uuid=uuid, email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        uuid: UUID = None,
        email: str = None,
        password: str = None,
        **extra_fields,
    ):
        """
        Create and save a User with the given email and password.
        """

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(
            uuid=uuid, email=email, password=password, **extra_fields
        )

    def create_superuser(
        self,
        uuid: UUID = None,
        email: str = None,
        password: str = None,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Active user must have is_active=True.")

        return self._create_user(
            uuid=uuid,
            email=email,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(db_column="uuid", primary_key=True, default=uuid4)
    email = models.EmailField(
        db_column="email",
        max_length=90,
        unique=True,
        db_index=True,
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
    uuid = models.UUIDField(db_column="uuid", primary_key=True, default=uuid4)
    user = models.OneToOneField(
        to="User", to_field="uuid", db_column="user", on_delete=models.CASCADE
    )
    name = models.CharField(
        db_column="name", max_length=50, blank=False, null=False
    )
    address = models.CharField(
        db_column="address", max_length=100, blank=False, null=False
    )
    phone_number = PhoneNumberField(
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


class Admin(models.Model):
    uuid = models.UUIDField(db_column="uuid", primary_key=True, default=uuid4)
    user = models.OneToOneField(
        to="User", to_field="uuid", db_column="user", on_delete=models.CASCADE
    )
    name = models.CharField(
        db_column="name", max_length=50, blank=False, null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "admins"
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
        ordering = ["-user__date_joined"]


class JWT(models.Model):
    """
    This model represents a JWT token in the system.
    """

    id = models.BigAutoField(db_column="id", primary_key=True)
    user = models.ForeignKey(
        db_column="user_id",
        to="User",
        to_field="uuid",
        on_delete=models.SET_NULL,
        db_index=True,
        null=True,
        blank=False,
    )
    jti = models.CharField(
        db_column="jti",
        max_length=255,
        unique=True,
        db_index=True,
        null=False,
        blank=False,
    )
    token = models.TextField(db_column="token", null=False, blank=False)
    date_joined = models.DateTimeField(
        db_column="date_joined", auto_now_add=True
    )
    expires_at = models.DateTimeField(
        db_column="expires_at", null=False, blank=False
    )

    class Meta:
        db_table = "jwt"
        verbose_name = "jwt"
        verbose_name_plural = "jwts"
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        return "Token for {} ({})".format(
            self.user,
            self.jti,
        )


class JWTBlacklisted(models.Model):
    """
    This model represents a blacklisted JWT token.
    """

    id = models.BigAutoField(db_column="id", primary_key=True)
    token = models.OneToOneField(
        db_column="token_id",
        to="JWT",
        to_field="id",
        on_delete=models.CASCADE,
    )
    date_joined = models.DateTimeField(
        db_column="date_joined", auto_now_add=True
    )

    class Meta:
        db_table = "jwt_blacklisted"
        verbose_name = "jwt_blacklisted"
        verbose_name_plural = "jwts_blacklisted"
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        return f"Blacklisted token for {self.token.user}"


class Pet(models.Model):
    uuid = models.UUIDField(db_column="uuid", primary_key=True, default=uuid4)
    type_pet = models.ForeignKey(
        to="TypePet",
        to_field="id",
        db_column="type_pet",
        on_delete=models.CASCADE,
    )
    shelter = models.ForeignKey(
        to="Shelter",
        to_field="uuid",
        db_column="shelter",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        db_column="name", max_length=50, blank=False, null=False
    )
    race = models.CharField(
        db_column="race", max_length=50, blank=False, null=False
    )
    age = models.IntegerField(db_column="age", blank=False, null=False)
    observations = models.CharField(
        db_column="observations", max_length=200, default="sin observaciones"
    )
    description = models.CharField(
        db_column="description", max_length=200, default="sin descripciones"
    )
    image = models.URLField(
        db_column="image",
        max_length=200,
        unique=True,
        default="https://imagedefault.com",
    )
    date_joined = models.DateTimeField(
        db_column="date joined", auto_now_add=True
    )

    class Meta:
        db_table = "pets"
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        return f"Pet {self.name} from Shelter {self.shelter.name}"


class TypePet(models.Model):
    id = models.BigAutoField(db_column="id", primary_key=True)
    name = models.CharField(
        db_column="name", max_length=50, blank=False, null=False
    )
    date_joined = models.DateTimeField(
        db_column="date joined", auto_now_add=True
    )

    class Meta:
        db_table = "type_pet"
        verbose_name = "TypePet"
        verbose_name_plural = "TypePets"
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        return f"Pet of type {self.name}"
