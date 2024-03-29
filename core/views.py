import json

from django.http import HttpResponse
from django.shortcuts import render
import telepot
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

TOKEN = "777893642:AAG3I_qD-yLxWHKdJzzOaua_CwFh5k6G4ME"
TelegramBot = telepot.Bot(TOKEN)

# Create your views here.
def index(request):
    return HttpResponse('ok')

class CommandReceiveView(View):

    def post(self, request):
        print(request.body)
        payload = json.loads(request.body.decode('utf-8'))
        chat_id = payload['message']['chat']['id']
        message = payload['message'].get('text')
        print(message)
        TelegramBot.sendMessage(chat_id, f"You said `${message}`")
        return JsonResponse({}, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommandReceiveView, self).dispatch(request, *args, **kwargs)