from django.db import models
from uuid import uuid4


class EmailsSent(models.Model):
    """
    This model represents the emails sent in the system.
    """

    uuid = models.UUIDField(
        db_column="uuid",
        primary_key=True,
        default=uuid4,
    )
    subject = models.CharField(
        db_column="subject",
        max_length=100,
        null=False,
        blank=False,
    )
    message = models.TextField(
        db_column="message",
        max_length=600,
        null=False,
        blank=False,
    )
    addressee = models.EmailField(
        db_column="addressee",
        max_length=90,
        db_index=True,
        null=False,
        blank=False,
    )
    additional_info = models.JSONField(
        db_column="additional_info",
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        db_column="date_joined", auto_now_add=True
    )

    class Meta:
        db_table = "emails_sent"
        verbose_name = "Email Sent"
        verbose_name_plural = "Emails Sent"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.uuid.__str__()
