from twiliosimple import Twilio, Utils, DjangoResponse
from django.http import HttpResponse
from django.shortcuts import render_to_response

def incoming_call(request):
	if is_valid_twilio_request(request):
		response = DjangoResponse()
		
		return response.say(
			'Thank you for calling TwilioSimple'
		).play(
		'example.mp3'
		).hangup()
	else:
		return HttpResponse(status=403)

print incoming_call('test')