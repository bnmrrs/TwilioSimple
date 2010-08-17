from twiliosimple import Twilio

# Account SID provided by Twilio
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Account Token provided by Twilio
account_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Sender number.  This must be a number that can send outgoing messages
sender = '5555555555'

# Number to send the message to
to = '5555555555'

# Body of the message
body 'This is a text message coming from Twilio!'

twilio = Twilio(account_sid, account_token)
outgoing_sms = twilio.sms(sender, to, body)

# Prints Twilio's response to our sms request
print outgoing_sms.get_response()
