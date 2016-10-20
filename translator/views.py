from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from microsofttranslator import Translator as BingTranslator

from .models import Translations
from . import config
import urllib.request as urlreq
import json

translator = BingTranslator(config.client_id, config.key)

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render(request=request))

def translate(request):
  body = json.loads(request.body.decode('utf-8'))
  data = {}
  data['original_text'] = body['text']
  data['language'] = translator.detect_language(body['text'])
  data['translated_text'] = translator.translate(body['text'], 'en')
  t = Translations(**data)
  t.save()
  return JsonResponse(data)


def retrieve(request):
  data = {}
  t = Translations.objects.values()
  data['data'] = [entry for entry in t] 
  return JsonResponse(data)