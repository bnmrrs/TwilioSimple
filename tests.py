import unittest
import re

import twiliosimple


class TwilioTest(unittest.TestCase):
	
	def strip(self, response):
	        return re.sub(r'\n|\t', '', str(response).strip())


class ResponseTests(TwilioTest):
	
	def test_very_basic_usage(self):
		"""Tests basic usage of the Response class"""
		r = twiliosimple.Response()
		self.failUnlessEqual(self.strip(r), """<Response/>""")
	
	
class SayTests(TwilioTest):

    def testEmptySay(self):
        """should be a say with no text"""
        r = twiliosimple.Response()
        r.say("")
        self.assertEquals(self.strip(r), '<Response><Say language="en" voice="woman"/></Response>')

    def testSayHelloWorld(self):
        """should say hello world"""
        r = twiliosimple.Response()
        r.say("Hello World")
        self.assertEquals(self.strip(r), '<Response><Say language="en" voice="woman">Hello World</Say></Response>')

    def testSayLoop(self):
        """should say hello world and loop 3 times"""
        r = twiliosimple.Response()
        r.say("Hello World", loop=3)
        self.assertEquals(self.strip(r), '<Response><Say language="en" loop="3" voice="woman">Hello World</Say></Response>')

    def testSayLoopWoman(self):
        """should say have a woman say hello monkey and loop 3 times"""
        r = twiliosimple.Response()
        r.say("Hello Monkey", loop=3, voice=twiliosimple.Response.VOICE_MAN)
        self.assertEquals(self.strip(r), '<Response><Say language="en" loop="3" voice="man">Hello Monkey</Say></Response>')


class TestPlay(TwilioTest):

    def testEmptyPlay(self):
        """should be an empty play"""
        r = twiliosimple.Response()
        r.play("")
        r = self.strip(r)
        self.assertEqual(r,"<Response><Play/></Response>")

    def testPlayHello(self):
        """should play hellomonkey.mp3"""
        r = twiliosimple.Response()
        r.play("http://hellomonkey.mp3")
        r = self.strip(r)
        self.assertEqual(r, "<Response><Play>http://hellomonkey.mp3</Play></Response>")

    def testPlayHelloLoop(self):
        """should play hellomonkey.mp3 three times"""
        r = twiliosimple.Response()
        r.play("http://hellomonkey.mp3", loop=3)
        r = self.strip(r)
        self.assertEqual(r, '<Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')


class TestRecord(TwilioTest):

    def testRecordEmpty(self):
        """should record"""
        r = twiliosimple.Response()
        r.record()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record finishOnKey="1234567890*#"/></Response>')

    def testRecordActionMethod(self):
        """should record with an action and a get method"""
        r = twiliosimple.Response()
        r.record(action="example.com", method=twiliosimple.Response.HTTP_METHOD_GET)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record action="example.com" finishOnKey="1234567890*#" method="GET"/></Response>')

    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = twiliosimple.Response()
        r.record(timeout=4, finish_on_key="#", max_length=30)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record finishOnKey="#" maxLength="30" timeout="4"/></Response>')

    def testRecordTranscribeCallback(self):
        """should record with a transcribe and transcribeCallback"""
        r = twiliosimple.Response()
        r.record(transcribe_callback="example.com")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record finishOnKey="1234567890*#" transcribe="true" transcribeCallback="example.com"/></Response>')


class TestRedirect(TwilioTest):

    def testRedirectMethod(self):
        r = twiliosimple.Response()
        r.redirect(url="example.com", method="POST")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect method="POST">example.com</Redirect></Response>')

    def testRedirectMethodGetParams(self):
        r = twiliosimple.Response()
        r.redirect(url="example.com?id=34&action=hey", method="POST")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect method="POST">example.com?id=34&amp;action=hey</Redirect></Response>')


class TestHangup(TwilioTest):

    def testHangup(self):
        """convenience: should Hangup to a url via POST"""
        r = twiliosimple.Response()
        r.hangup()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Hangup/></Response>')


class TestSms(TwilioTest):

    def testToFromAction(self):
        """ Test the to, from, and status callback"""
        r = twiliosimple.Response()
        r.sms("Hello, World", receiver_num=1231231234, sender_num=3453453456, 
            status_callback="example.com?id=34&action=hey")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Sms from="3453453456" statusCallback="example.com?id=34&amp;action=hey" to="1231231234">Hello, World</Sms></Response>')


class TestDial(TwilioTest):

    def testDial(self):
        """ should redirect the call"""
        r = twiliosimple.Response()
        r.dial("1231231234")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial>1231231234</Dial></Response>')

    def testAddNumber(self):
        """add a number to a dial"""
        r = twiliosimple.Response()
        d = twiliosimple.Dial()
        d.number("1231231234")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Number>1231231234</Number></Dial></Response>')

    def testAddConference(self):
        """ add a conference to a dial"""
        r = twiliosimple.Response()
        d = twiliosimple.Dial()
        d.conference("My Room")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Conference>My Room</Conference></Dial></Response>')


class TestGather(TwilioTest):

    def testBasic(self):
        """ a gather with nothing inside"""
        r = twiliosimple.Response()
        r.gather('example.org')
        r = self.strip(r)
        self.assertEquals(r, '<Response><Gather action="example.org" finishOnKey="#" method="GET" numDigits="1" timeout="5"/></Response>')

    def testNestedSayPlayPause(self):
        """ a gather with a say, play, and pause"""
        r = twiliosimple.Response()
        g = twiliosimple.Gather()
        g.say("Hey")
        g.play("hey.mp3")
        g.pause()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause/></Gather></Response>')

if __name__ == '__main__':
	unittest.main()