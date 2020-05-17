from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse


@csrf_exempt
def answer(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    vr.say('Hello! Hello! Hello! Hello! Hello! Hello! Hello! Hello! Hello! Hello!')
    return HttpResponse(str(vr), content_type='text/xml')