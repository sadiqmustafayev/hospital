from django.db import models
from django.utils.translation import gettext_lazy as _


class AnalizRaport(models.Model):
  name_surname = models.CharField(max_length=200)
  aciklama = models.CharField()
  date = models.DateTimeField(auto_now_add=True)
  dosya = models.ImageField(upload_to='Report_files/', blank=True)

  def __str__(self):
    return self.name_surname

  class Meta:
     permissions = (('can_add_raport', 'Can add raport'), )

