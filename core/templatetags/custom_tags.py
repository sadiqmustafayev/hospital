from django import template

from core.models import Blogs, Doctors

register = template.Library()


@register.simple_tag
def get_blogs(offset, limit):
  return Blogs.objects.filter(is_published=True)[offset:limit]


@register.simple_tag
def get_doctors(offset, limit):
  return Doctors.objects.filter(is_published=True)[offset:limit]
