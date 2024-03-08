from django.shortcuts import render, get_object_or_404, redirect
from raport.models import AnalizRaport
from raport.forms import AnalizRaportForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from raport.models import AnalizRaport
from core.models import Setting
from django.core.paginator import Paginator
from django.db.models import Max
import random
import os
from django.utils.translation import gettext as _

def rapor_detay(request, rapor_id):
  rapor = get_object_or_404(AnalizRaport, id=rapor_id)
  context = {'rapor': rapor, 'setting': Setting.objects.first(),'report_count': AnalizRaport.objects.count()}
  return render(request, 'rapor_detay.html', context)


def rapor_search(request):

  if 'analiz_id' in request.GET and request.GET['analiz_id']:
    try:
      analiz_id = int(request.GET['analiz_id'])
      rapor = AnalizRaport.objects.get(id=analiz_id)
      return redirect('rapor_detay', rapor_id=rapor.id)
    except (ValueError, AnalizRaport.DoesNotExist):
      error_message = _("Invalid raport ID")
      return render(request, 'rapor_search.html', {
        'error_message': error_message,
        'setting': Setting.objects.first(),
        'report_count': AnalizRaport.objects.count()

      })
  return render(request, 'rapor_search.html',
                {'setting': Setting.objects.first()})


@user_passes_test(lambda u: u.has_perm('raport.can_add_raport'))
def rapor_add(request):
  max_rapor_id = AnalizRaport.objects.aggregate(Max('id'))['id__max']
  used_rapor_ids = set(AnalizRaport.objects.values_list('id', flat=True))
  # id eyni olduqda yenisin yaradir
  if request.method == "POST":
    form = AnalizRaportForm(request.POST, request.FILES)
    if form.is_valid():
      rapor = form.save(commit=False)
      while True:
        rapor_id = random.randint(10000, 9999999)
        if rapor_id not in used_rapor_ids:
          break
      rapor.id = rapor_id

      #file adi raport id ile eynilesdirilir
      dosya_adi, dosya_uzantisi = os.path.splitext(rapor.dosya.name)
      rapor.dosya.name = f"{rapor.id}{dosya_uzantisi}"
      rapor.save()

      return redirect('rapor_detay', rapor_id=rapor.id)
  else:
    form = AnalizRaportForm()

  return render(request, 'rapor_add.html', {
    'form': form,
    'setting': Setting.objects.first(),
    'report_count': AnalizRaport.objects.count()
  })


@user_passes_test(lambda u: u.has_perm('raport.can_add_raport')
                  )  #admin pannelde analiz group
def rapor_list(request):
  raporlar = AnalizRaport.objects.all()

  if 'search' in request.GET:
    search_term = request.GET['search']
    if search_term.isdigit():
      raporlar = raporlar.filter(id=search_term)
    else:
      raporlar = raporlar.filter(name_surname__icontains=search_term)

  paginator = Paginator(raporlar, 10)  # Show 10 raporlar per page
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  context = {'page_obj': page_obj, 'setting': Setting.objects.first(),'report_count': AnalizRaport.objects.count()}
  return render(request, 'rapor_list.html', context)
