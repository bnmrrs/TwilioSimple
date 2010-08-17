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


import simplejson as json

import exceptions

class OutgoingCall:
  def __init__(self, call_response):
    self.raw_response = call_response
    self.validated_response = self.validate_response(call_response)
    self.load_response(self.loaded_response)

  def validate_response(self, response):
    try:
      response = json.loads(response)
    except ValueError:
      raise InvalidResponse('Response was not a valid JSON document')

    if not 'TwilioResponse' in response:
      raise InvalidResponse('Twilio Response was not included')

    if 'RestException' in response['TwilioResponse']:
      raise RestException(response['TwilioResponse']['RestException']['Message'])

    if not 'Call' in response['TwilioResponse']:
      raise InvalidResponse('Call body was not included in the response')

    return response

  def load_response(self, response):
    self.loaded_response = {
        'call_sid': response['TwilioResponse']['Call']['Sid'],
        'account_sid': response['TwilioResponse']['Call']['AccountSid'],
        'called': response['TwilioResponse']['Call']['Called'],
        'caller': response['TwilioResponse']['Call']['Caller'],
        'phone_number_sid': response['TwilioResponse']['Call']['PhoneNumberSid'],
        'status': response['TwilioResponse']['Call']['Status'],
        'start_time': response['TwilioResponse']['Call']['StartTime'],
        'end_time': response['TwilioResponse']['Call']['EndTime'],
        'price': response['TwilioResponse']['Call']['Price'],
        'flags': response['TwilioResponse']['Call']['Flags']
    }

  def get_response(self):
    return self.loaded_response

  def get_raw_response(self):
    return self.raw_response
