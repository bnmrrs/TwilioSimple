import twilio as twilio_official

from twiliosimple.outgoing import OutgoingCall

class Twilio:
  def __init__(self, id, token):
    self.id = id
    self.token = token
    self.api_version = '2008-08-01'

    self.account = twilio_official.Account(id, token)

  def call(self, caller, number, callback_url, details={}):
    api_endpoint = '%s/Accounts/%s/Calls.json' % (self.api_version, self.id)

    details.update({
      'Caller': caller,
      'Called': number,
      'Url': callback_url,
    })

    return OutgoingCall(self.account.request(api_endpoint, 'POST', details))

