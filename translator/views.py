from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from microsofttranslator import Translator

from .models import Translations
from . import config
import urllib.request as urlreq
import json

translator = Translator(config.client_id, config.key)

def index(request):
  template = loader.get_template('translator/index.html')
  return HttpResponse(template.render(request=request))

def translate(request):
  body = json.loads(request.body.decode('utf-8'))
  print(body)
  data = {}
  data['original_text'] = body['text']
  data['language'] = translator.detect_language(body['text'])
  data['translation'] = translator.translate(body['text'], 'en')
  return JsonResponse(data)


def getTranslations(request):
  pass