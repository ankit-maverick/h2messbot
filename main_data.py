#!/usr/bin/env python
 
import cgi
from google.appengine.api import xmpp
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
 
class XMPPHandler(webapp.RequestHandler):
    def post(self):
        message = xmpp.Message(self.request.POST)
        sender = cgi.escape(self.request.get('from')).split("/")[0]
        bodystart = message.body.lower()[0:2]

        with open('data.txt') as f:
            content = f.readlines()

        if bodystart == 'mo':
            message.reply(content[0] + '\n' + content[1] + '\n' + content[2] + '\n' + content[3] + '\n' + content[4] + '\n')

        elif bodystart == 'tu':
            message.reply(content[5] + '\n' + content[6] + '\n' + content[7] + '\n' + content[8] + '\n' + content[9] + '\n')

        elif bodystart == 'we':
            message.reply(content[10] + '\n' + content[11] + '\n' + content[12] + '\n' + content[13] + '\n' + content[14] + '\n')

        elif bodystart == 'th':
            message.reply(content[15] + '\n' + content[16] + '\n' + content[17] + '\n' + content[18] + '\n' + content[19] + '\n')

        elif bodystart == 'fr':
            message.reply(content[20] + '\n' + content[21] + '\n' + content[22] + '\n' + content[23] + '\n' + content[24] + '\n')

        elif bodystart == 'sa':
            message.reply(content[25] + '\n' + content[26] + '\n' + content[27] + '\n' + content[28] + '\n' + content[29] + '\n')

        elif bodystart == 'su':
            message.reply(content[30] + '\n' + content[31] + '\n' + content[32] + '\n' + content[33] + '\n' + content[34] + '\n')

        else :
            message.reply('Invalid query!! Enter the first two letters of the day of the week. For example, enter `sa` for Saturday\'s menu.')

application = webapp.WSGIApplication([('/_ah/xmpp/message/chat/', XMPPHandler)],
                                     debug=True)
 
def main():
    run_wsgi_app(application)
 
if __name__ == "__main__":
    main()
