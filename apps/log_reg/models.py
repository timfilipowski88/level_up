from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
import bcrypt

EMAIL_REGEX = re.compile(
    '^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

# Create your models here.

def lengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(_('{} must be longer than: 2'.format(value)))

def lengthGreaterThanSeven(value):
    if len(value) < 8:
        raise ValidationError(_(
            '{} must be longer than: 7'.format(value)
        ))

def validEmail(value):
    if not EMAIL_REGEX.match(value):
        raise ValidationError(_(
            '{} must be valid email format like abc123@site.abc'.format(value)
        ))

def passwordMatch(value):
    pass


class User(models.Model):
    first_name = models.CharField(max_length=45, validators = [lengthGreaterThanTwo])
    last_name = models.CharField(max_length=45, validators=[lengthGreaterThanTwo])
    username = models.CharField(max_length=45, validators=[lengthGreaterThanTwo])
    email = models.EmailField(max_length=150, validators=[validEmail])
    password = models.CharField(max_length=150, validators=[lengthGreaterThanSeven, passwordMatch])
