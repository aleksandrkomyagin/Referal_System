from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Логин",
        max_length=settings.MAX_LEN_USERNAME_USER_MODEL,
        blank=True,
        unique=True,
    )
    email = models.CharField(
        verbose_name="Почта",
        max_length=settings.MAX_LEN_EMAIL_USER_MODEL,
        blank=False,
        unique=True,
    )
    password = models.CharField(
        verbose_name="Пароль",
        max_length=settings.MAX_LEN_HASH_PASSWORD_USER_MODEL,
        blank=False,
    )
    invite_code = models.CharField(
        verbose_name="Инвайт-код",
        max_length=settings.INVITE_CODE_LENGTH,
        blank=True,
        null=True,
        editable=False,
    )
    inviter = models.ForeignKey(
        "self",
        related_name="invitings",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("username",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
