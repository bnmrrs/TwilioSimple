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

import urllib2
import simplejson as json

import twilio as twilio_official

from outgoing import OutgoingCall, OutgoingSMS

class Twilio:
	
  def __init__(self, id, token):
    self.id = id
    self.token = token
    self.api_version = '2008-08-01'

    self.account = twilio_official.Account(id, token)


  def call(self, caller, called, callback_url, details={}):
    api_endpoint = '%s/Accounts/%s/Calls.json' % (self.api_version, self.id)

    details.update({
      'Caller': caller,
      'Called': called,
      'Url': callback_url,
    })

    try:
      call_response = self.account.request(api_endpoint, 'POST', details)
    except urllib2.HTTPError, e:
      call_response = e.read()

    return OutgoingCall(call_response)


  def sms(self, from_num, to, body, callback=False):
    api_endpoint = '%s/Accounts/%s/SMS/Messages.json' % (self.api_version, self.id)

    details = {
      'From': from_num,
      'To': to,
      'Body': body
    }

    if callback:
      details.update({ 'StatusCallback': callback })

    try:
      sms_response = self.account.request(api_endpoint, 'POST', details)
    except urllib2.HTTPError, e:
      sms_response = e.read()

    return OutgoingSMS(sms_response)
