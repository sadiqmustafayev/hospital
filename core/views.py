from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from core.forms import ContactForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models import Q
from baseuser.models import BaseUser
from celery import shared_task
from django.contrib.auth.decorators import user_passes_test, login_required
from django.conf import settings
from .models import Blogs, Doctors, Setting, Subscriber, Contact, Comment
from raport.models import AnalizRaport
from django.utils.translation import gettext as _
from .forms import CommentForm



def home(request):
  context = {
    'setting': Setting.objects.first(),
    'doctor_count': Doctors.objects.count(),
    'user_count': BaseUser.objects.count(),
    'contact_count': Contact.objects.count(),
    'report_count': AnalizRaport.objects.count()
  }
  return render(request, 'home.html', context)


def about(request):
  context = {
    'setting': Setting.objects.first(),
    'doctor_count': Doctors.objects.count(),
    'user_count': BaseUser.objects.count(),
    'contact_count': Contact.objects.count(),
    'report_count': AnalizRaport.objects.count()
  }
  return render(request, 'about.html', context)


def appointment(request):
  context = {
    'setting': Setting.objects.first(),
    'doctor_count': Doctors.objects.count(),
    'user_count': BaseUser.objects.count(),
    'contact_count': Contact.objects.count(),
    'report_count': AnalizRaport.objects.count()
  }
  return render(request, 'appointment.html', context)


def base(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
    'report_count': AnalizRaport.objects.count()
  }
  return render(request, 'index.html', context)


def blog_details(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
    'report_count': AnalizRaport.objects.count()
  }
  return render(request, 'blog_details.html', context)


def booking_list(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
    'report_count': AnalizRaport.objects.count()
  }
  return render(request, 'booking_list.html', context)


# def contact(request):
#   context = {
#     'setting': Setting.objects.first(),
#     'contact_count': Contact.objects.count(),
#     'report_count': AnalizRaport.objects.count()
#   }
#   return render(request, 'contact.html', context)


def error(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
  }
  return render(request, 'error.html', context)


def faq(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
  }
  return render(request, 'faq.html', context)


def index_2(request):
  context = {'title': 'None', 'setting': Setting.objects.first()}
  return render(request, 'index_2.html', context)


def service_details(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
  }
  return render(request, 'service_details.html', context)


def service(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
  }
  return render(request, 'service.html', context)


def services(request):
  context = {
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
  }
  return render(request, 'services.html', context)


class BlogsListView(ListView):
  model = Blogs
  template_name = 'blog.html'
  context_object_name = 'blog'
  paginate_by = 2

  def get_queryset(self):
    return Blogs.objects.filter(is_published=True)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['setting'] = Setting.objects.first()
    context['contact_count'] = Contact.objects.count()
    context['report_count'] = AnalizRaport.objects.count()
    return context

  def get_paginate_by(self, queryset):
    paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
    if paginate_by:
      return int(paginate_by)
    return self.paginate_by


class DoctorsListView(ListView):
  model = Doctors
  template_name = 'doctor.html'
  context_object_name = 'doctor'
  paginate_by = 6

  def get_queryset(self):
    return Doctors.objects.filter(is_published=True)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['setting'] = Setting.objects.first()
    context['doctor_count'] = Doctors.objects.count()
    context['user_count'] = BaseUser.objects.count()
    context['contact_count'] = Contact.objects.count()
    context['report_count'] = AnalizRaport.objects.count()
    return context

  def get_paginate_by(self, queryset):
    paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
    if paginate_by:
      return int(paginate_by)
    return self.paginate_by


def blog_details(request, slug):
  blog = Blogs.objects.get(slug=slug)
  context = {'blog': blog, 'setting': Setting.objects.first()}
  return render(request, 'blog_details.html', context)


def doctor_details(request, slug):
  doctor = Doctors.objects.get(slug=slug)
  context = {
    'doctor': doctor,
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count(),
    'doctor_count': Doctors.objects.count(),
    'user_count': BaseUser.objects.count(),
    'report_count': AnalizRaport.objects.count()
  }
  return render(request, 'doctor_details.html', context)


def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      #FORM DATA
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']

      # E-MAIL message  CREATE
      subject = _('New Contact Form Received')
      body = f'Name: {name}\nE-mail: {email}\nMessage: {message}'
      from_email = settings.DEFAULT_FROM_EMAIL
      recipient_list = [Setting.objects.first().contact_form_email
                        ]  #settings modelinden gelir :D

      # E-mail send
      send_mail(subject, body, from_email, recipient_list, fail_silently=True)

      #forward
      return HttpResponseRedirect(reverse('thank-you'))
  else:
    form = ContactForm()

  context = {
    'setting': Setting.objects.first(),
    'doctor_count': Doctors.objects.count(),
    'user_count': BaseUser.objects.count(),
    'report_count': AnalizRaport.objects.count(),
    'contact_count': Contact.objects.count(),
        'contact': form,
    'message': _('Message has been sent successfully!')
  }

  return render(request, 'contact.html', context)


def thank_you(request):
  context = {
    'setting': Setting.objects.first(),
    'message': _('Message has been sent successfully!')
  }
  return render(request, 'thank_you.html', context)


def search_doctors(request):
  query = request.GET.get('q')
  if query:
    doctors = Doctors.objects.filter(name__icontains=query)
    

  else:
    doctors = []
  context = {
    'doctors': doctors,
    'query': query,
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count()
  }
  
  return render(request, 'search_doctors.html', context)


def site_search(request):
  query = request.GET.get('site_search')
  if query:
    doctors = Doctors.objects.filter(name__icontains=query)
    blogs = Blogs.objects.filter(title__icontains=query)
  else:
    doctors = []
    blogs = []
  context = {
    'doctors': doctors,
    'blogs': blogs,
    'query': query,
    'setting': Setting.objects.first(),
    'contact_count': Contact.objects.count()
  }
  return render(request, 'site_search.html', context)


@shared_task
@user_passes_test(lambda u: u.has_perm('subscriber.can_send_email'))
def send_email(request):
  setting = Setting.objects.first()

  if request.method == 'POST':
    recipient_list = []
    to_subscribers = request.POST.get('to_subscribers')
    to_baseusers = request.POST.get('to_baseusers')
    to_contacts = request.POST.get('to_contacts')
    subject = request.POST['subject']
    message = request.POST['message']
    sender = 'your-email@example.com'

    if 'recipient_list[]' in request.POST:
      recipient_list = request.POST.getlist('recipient_list[]')

    if to_subscribers:
      subscribers = Subscriber.objects.filter(is_active=True)
      subscriber_emails = subscribers.values_list('email', flat=True)
      recipient_list += list(subscriber_emails)

    if to_baseusers:
      baseuser_emails = BaseUser.objects.filter(
        Q(is_active=True) & Q(email__isnull=False)).values_list('email',
                                                                flat=True)
      recipient_list += list(baseuser_emails)

    if to_contacts:
      contact_emails = Contact.objects.filter(
        Q(email__isnull=False)).values_list('email', flat=True)
      recipient_list += list(contact_emails)

    recipient_list = list(set(recipient_list))

    send_mail(
      subject,
      message,
      sender,
      recipient_list,
      fail_silently=False,
    )

    context = {
      'message': _('Email has been sent successfully!'),
      'setting': setting,
      'contact_count': Contact.objects.count(),
          'user_count': BaseUser.objects.count(),
    'subscriber_count': Subscriber.objects.count(),
    }
    return render(request, 'email_sent.html', context)

  return render(request, 'send_email.html', {'user_count': BaseUser.objects.count(),'subscriber_count': Subscriber.objects.count(),'setting': setting,'contact_count': Contact.objects.count()})



@login_required
def add_comment(request, slug):
    blog = get_object_or_404(Blogs, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, 'Your comment was successfully added.')
            return redirect('blog_details', slug=blog.slug)
    else:
        form = CommentForm()

    return render(request, 'blog_details.html', {'blog': blog, 'form': form})


