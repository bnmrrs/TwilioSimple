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


class Response:
	_response = ""
	
	def say(self, to_say):
		self._response += "<Say>%s</Say>" % (to_say)
		
		return self
		
	def play(self, to_play):
		self._response += "<Play>%s</Play>" % (to_play)
		return self
		
	def redirect_get(self):
		pass
		
	def gather(self, action_url, num_digits=1, finish_on_key='#', timeout=5, method='POST'):
		self._response += "<Gather action='%s' numDigits='%d' finishOnKey='%s' timeout='%d' method='%s' />" \
			% (action_url, num_digits, finish_on_key, timeout, method)
		return self
		
	def record(self, action_url, max_length=60, finish_on_key='#', timeout=5, method='POST'):
		self._response += "<Record action='%s' maxLength='%d' finishOnKey='%s' timeout='%d' method='%s' />" \
			% (action_url, max_length, finish_on_key, timeout, method)
		return self
		
	def hangup(self):
		self._response += '<Hangup />'
		return self
		
	def dial(self):
		pass
		
	def get_response(self):
		return "<?xml version='1.0'?><Response>%s</Response>" % (self._response)
		
	def print_response(self):
		print self.get_response() 