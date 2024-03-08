from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .utils import slugify_KNN
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

from django.db import models

class raport_analizraport(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Diğer alanlar...



class BlogImage(models.Model):
  blog = models.ForeignKey("Blogs",
                           on_delete=models.CASCADE,
                           related_name='images')
  image = models.ImageField(upload_to='blogs')

  class Meta:
    verbose_name = 'Blog Image'
    verbose_name_plural = 'Blog Images'

  def __str__(self):
    return self.blog.title + ' Image'

  def __str__(self):
    return f"{self.blog.title} - {self.image.name}"


class Basemodel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Setting(Basemodel):
  number1 = PhoneNumberField(max_length=20, blank=False)
  number2 = PhoneNumberField(max_length=20, blank=False)
  e_mail = models.EmailField()
  facebook = models.URLField(max_length=100, null=True, blank=True)
  instagram = models.URLField(max_length=100, null=True, blank=True)
  twitter = models.URLField(max_length=100, null=True, blank=True)
  linkedin = models.URLField(max_length=100, null=True, blank=True)
  logo = models.ImageField(upload_to="logo")
  creator = models.CharField(max_length=20)
  address1 = models.CharField(max_length=20)
  address2 = models.CharField(max_length=20)
  contact_form_email = models.EmailField()
  location = models.URLField(max_length=2000)
  slogan = models.CharField(max_length=2000)

  def __str__(self):
    return "Setting"

  class Meta:
    verbose_name = _("Setting")
    verbose_name_plural = _("Settings")


class News(Basemodel):
  title = models.CharField(max_length=200)
  content = RichTextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='news_images', blank=True, null=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
  category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = _("News")
    verbose_name_plural = _("News")


class Category(Basemodel):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = _("Category")


class Tag(Basemodel):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = _("Tag")


class NewsTag(Basemodel):
  news = models.ForeignKey(News, on_delete=models.CASCADE)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.tag} tag for the news {self.news}"

  class Meta:
    verbose_name_plural = _("NewsTag")


class Page(Basemodel):
  title = models.CharField(max_length=200)
  content = RichTextField()
  slug = models.SlugField(max_length=100, unique=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = _("Page")
    verbose_name_plural = _("Page")


class Story(Basemodel):
  title = models.CharField(max_length=100)
  description = RichTextField()
  image = models.ImageField(upload_to="stories")
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = _("Story")
    verbose_name_plural = _("Stories")


class Blogs(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True, blank=True)
  description = RichTextField()
  created_at = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  is_published = models.BooleanField(default=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
  image = models.ImageField(upload_to='blogs')

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify_KNN(self.title)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('blog_detail', args=[str(self.slug)])

  class Meta:
    verbose_name = _('Blogs')
    verbose_name_plural = _('Blogs')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    @staticmethod
    def search_feed(query):
        return Comment.objects.filter(text__icontains=query)

    class Meta:
        ordering = ('-created_at', )
        


class Contact(Basemodel):

  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone_number = models.CharField(max_length=100)
  message = models.CharField(max_length=100000)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _("Contact")
    verbose_name_plural = _("Contact")


class Positions(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _("Position")
    verbose_name_plural = _("Positions")


class Doctors(models.Model):
  name = models.CharField(max_length=50)
  age = models.CharField(max_length=2)
  email = models.EmailField()
  slug = models.SlugField(unique=True, blank=True)
  number = models.CharField(max_length=15)
  facebook = models.URLField(max_length=100)
  instagram = models.URLField(max_length=100)
  twitter = models.URLField(max_length=100)
  experience = models.CharField(max_length=2)
  is_published = models.BooleanField(default=True)
  image = models.ImageField(upload_to='Doctors')
  educational_history = RichTextField(max_length=10000, null=True, default=" ")
  positions = models.ForeignKey(Positions, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify_KNN(self.name)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('doctor_detail', args=[str(self.slug)])

  class Meta:
    verbose_name = _("Doctor")
    verbose_name_plural = _("Doctors")


class Subscriber(Basemodel):
  email = models.EmailField()
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.email

  class Meta:
    permissions = (('can_send_email', 'Can Send Email'), )

