from TwilioSimple import Twilio

# Account SID provided by Twilio
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Account Token provided by Twilio
account_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Number to appear on caller id.  This number must be either provided by
# Twilio or verifided through the web interface
callout_num = '5555555555'

# Number for Twilio to call
num_to_call = '5555555555'

# Callback URL for Twilio to use
callback = 'http://example.org/callback.py'

twilio = Twilio(account_sid, account_token)
outgoing_call = twilio.call(callout_num, num_to_call, callback)

# Prints Twilio's response to our call request
print outgoing_call.get_response()