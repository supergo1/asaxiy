from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


def phone_validator(value):
    if value.startswith('+998') and len(value) == 13:
        return True
    else:
        raise ValidationError('Telefon nomer +998 bilan boshlanishi kerak va 13ta shrit bolishi kerak')


class User(AbstractUser):
    phone = models.CharField(max_length=13, validators=[phone_validator])
    avatar = models.ImageField(upload_to='avatar/')

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    ball = models.IntegerField(default=0)
    account_id = models.CharField(max_length=32, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.account_id = f"A{self.id}{self.user.id}"
        super(Balance, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}"












