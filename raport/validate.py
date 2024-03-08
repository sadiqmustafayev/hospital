from django.utils.translation import gettext as _
from django import forms
import os


def validate_KNN(value):
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.pdf']
  if not ext.lower() in valid_extensions:
    raise forms.ValidationError(
      _('Unsupported file extension. Only {} are supported.').format(
        ', '.join(valid_extensions)))
