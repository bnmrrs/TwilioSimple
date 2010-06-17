import simplejson as json

import twiliosimple.exceptions

class OutgoingCall:
  def __init__(self, call_response):
    self.raw_response = call_response
    self.loaded_response = json.loads(call_response)

    self.validate_response(self.loaded_response)
    self.load_response(self.loaded_response)

  def validate_response(self, response):
    if not 'TwilioResponse' in response:
      raise InvalidResponse('Twilio Response was not included')

    if 'RestException' in response['TwilioResponse']:
      raise RestException(response['TwilioResponse']['RestException']['Message'])

    if not 'Call' in response['TwilioResponse']:
      raise InvalidResponse('Call body was not included in the response')

  def load_response(self, response):

    self.call_sid = response['TwilioResponse']['Call']['Sid']
    self.account_sid = response['TwilioResponse']['Call']['AccountSid']
    self.called = response['TwilioResponse']['Call']['Called']
    self.caller = response['TwilioResponse']['Call']['Caller']
    self.phone_number_sid = response['TwilioResponse']['Call']['PhoneNumberSid']
    self.status = response['TwilioResponse']['Call']['Status']
    self.start_time = response['TwilioResponse']['Call']['StartTime']
    self.end_time = response['TwilioResponse']['Call']['EndTime']
    self.price = response['TwilioResponse']['Call']['Price']
    self.flags = response['TwilioResponse']['Call']['Flags']

  def get_response(self):
    return self.loaded_response

  def get_raw_response(self):
    return self.raw_response
