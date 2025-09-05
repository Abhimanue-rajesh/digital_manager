from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """This model should be used as the base for both the applicant and the customer also
    can use this for the employee by switching the is_staff status to be true"""

    USER_TYPE_CHOICES = (
        ("admin", "Admin"),
        ("designer", "Designer"),
        ("digital_marketing_expert", "Digital Marketing Expert"),
        ("manager", "Manager"),
    )

    user_type = models.CharField(max_length=24, choices=USER_TYPE_CHOICES)
    can_approve = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}  ({self.get_user_type_display()})"

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(
            ("pbkdf2_sha256$", "bcrypt$", "argon2")
        ):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Notification(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.content[:20]}.. {self.is_read}"
