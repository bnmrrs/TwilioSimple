class TwilioSimpleException(Exception):
  pass

class InvalidResponse(TwilioSimpleException):
  pass

class RestException(TwilioSimpleException):
  pass

