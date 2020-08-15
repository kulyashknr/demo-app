import os
from django.core.exceptions import ValidationError


def validate_file_size(value):
    if value.size > 1000000:
        raise ValidationError('max file size: 1Mb')

