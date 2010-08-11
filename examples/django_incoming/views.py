from TwilioSimple import Twilio, Utils, Response
from django.http import HttpResponse
from django.shortcuts import render_to_response

def incoming_call(request):
	if is_valid_twilio_request(request):
		response = Response()
		
		response.say(
			'Thank you for calling TwilioSimple'
		).play(
		'example.mp3'
		).hangup()
		
		return render_to_response('templates/incoming_call.html', {
			'response': response.get_response
		})
	else:
		return HttpResponse(status=403)
