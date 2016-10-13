from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Translations

def index(request):
  template = loader.get_template('translator/index.html')
  return HttpResponse(template.render(request=request))

def translate(request):
  print(request)
  return JsonResponse({})

def getTranslations(request):
  pass