#!/usr/bin/env python
#
#  The MIT License
#
#  Copyright (c) 2009 Ben Morris
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

import twilio as twilio_official

class Response:
	
	VOICE_WOMAN = 'woman'
	VOICE_MAN = 'man'
	
	LANGUAGE_ENGLISH = 'en'
	LANGUAGE_SPANISH = 'es'
	LANGUAGE_FRENCH = 'fr'
	LANGUAGE_GERMAN = 'de'
	
	HTTP_METHOD_POST = 'POST'
	HTTP_METHOD_GET = 'GET'
	
	REASON_REJECTED = 'rejected'
	REASON_BUSY = 'busy'
	
	def __init__(self):
		self.twilio_response = twilio_official.Response()
		
	def __str__(self):
		return self.getcontent()
		
	def getcontent(self):
		return str(self.twilio_response)
			
	def get_last_verb(self):
		return self.last_verb
			
	def say(self, to_say, voice=VOICE_WOMAN, language=LANGUAGE_ENGLISH, 
			loop=0):
		self.last_verb = twilio_official.Say(to_say, voice, language, loop)
		self.twilio_response.append(self.last_verb)
		
		return self
			
	def play(self, to_play, loop=0):
		self.last_verb = twilio_official.Play(to_play, loop)
		self.twilio_response.append(self.last_verb)
		
		return self
			
	def pause(self, length):
		self.last_verb = twilio_official.Pause(length)
		self.twilio_response.append(self.last_verb)
		
		return self
			
	def redirect(self, url, method=HTTP_METHOD_GET):
		self.last_verb = twilio_official.Redirect(url, method)
		self.twilio_response.append(self.last_verb)
		
		return self
			
	def hangup(self):
		self.last_verb = twilio_official.Hangup()
		self.twilio_response.append(self.last_verb)
		
		return self
			
	def gather(self, action_url, method=HTTP_METHOD_GET, num_digits=1, 
				finish_on_key='#', timeout=5):
		self.last_verb = twilio_official.Gather(action_url, method, num_digits, \
			timeout, finish_on_key)
		self.twilio_response.append(self.last_verb)
		
		return self
			
	def number(self, number, send_digits=None):
		self.last_verb = twilio_official.Number(number, send_digits)
		self.twilio_response.append(self.last_verb)
		
		return self
		
	def sms(self, msg, receiver_num, sender_num, method=None, action_url=None, 
			status_callback=None):
		self.last_verb = twilio_official.Sms(msg, receiver_num, sender_num, \
			method, action_url, status_callback)
		self.twilio_response.append(self.last_verb)
		
		return self
		
	def conference(self, name, muted=None, beep=None, start_on_enter=None, 
					end_on_exit=None, wait_url=None, wait_method=None):
		self.last_verb = twilio_official.Conference(name, muted, beep,\
			start_on_enter, end_on_exit, wait_url, wait_method)
		self.twilio_response.append(self.last_verb)
		
		return self
		
	def dial(self, number, action=None, method=None):
		self.last_verb = twilio_official.Dial(number, action, method)
		self.twilio_response.append(self.last_verb)
		
		return self
		
	def record(self, action=None, method=None, max_length=None, timeout=None,
				transcribe_callback=None, finish_on_key="1234567890*#"):
		if transcribe_callback:
			self.last_verb = twilio_official.Record(action, method, max_length, \
				timeout, transcribeCallback=transcribe_callback, \
				transcribe="true", finishOnKey=finish_on_key)
		else:
			self.last_verb = twilio_official.Record(action, method, max_length, \
				timeout, finishOnKey=finish_on_key)	
		self.twilio_response.append(self.last_verb)
		
		return self
		
	def reject(self, reason=REASON_REJECTED):
		self.last_verb = twilio_official.Reject(reason)
		self.twilio_response.append(self.last_verb)
		
		return self