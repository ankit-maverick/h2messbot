#!/usr/bin/env python
 
import cgi
from google.appengine.api import xmpp
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
 
class XMPPHandler(webapp.RequestHandler):
    def post(self):
        message = xmpp.Message(self.request.POST)
        sender = cgi.escape(self.request.get('from')).split("/")[0]
        body = message.body
        
        if body.lower() == 'mo':
            message.reply('17 Feb : Monday\n\nBREAKFAST : Upma, BBJO, Coconut chutney, Chocos\n\nLUNCH : Rajma, DRR, Masala papad, Curd rice\n\nTIFFIN : Sabudana Wada, Banana Shake\n\nDINNER : Palak paneer, Egg curry, Tava paratha, Rice, Dal, Sweet')

        elif body.lower() == 'tu':
            message.reply('18 Feb : Tuesday\n\nBREAKFAST : Puri Bhaji, BBJ, Cornflakes, Boiled egg\n\nLUNCH : Kadi pakoda, Aloo jeera, Roti, Rasna, Fruit\n\nTIFFIN : Veg cheese sandwich\n\nDINNER : Paneer paratha, Dal makhani, Lemon Rice, Ice cream, Schezwan chutney')

        elif body.lower() == 'we':
            message.reply('19 Feb : Wednesday\n\nBREAKFAST : Poha, BBJO, Cornflakes\n\nLUNCH : Chole Bhature, Jeera rice, Imli chutney, Boondi raita\n\nTIFFIN : Vada sambhar, Coconut chutney\n\nDINNER : Gobi matar, Rice-roti, Chicken Lollipop, Corn soup')

        elif body.lower() == 'th':
            message.reply('20 Feb : Thursday\n\nBREAKFAST : Cheela, Green chutney, Cornflakes, BBJ, Egg bhurji\n\nLUNCH : Bhindi masala, DRR, Marconi salad, Roasted papad\n\nTIFFIN : Onion Kachori\n\nDINNER : Malai kofta, Dal, Roti, Masala Rice, Custard')

        elif body.lower() == 'fr':
            message.reply('21 Feb : Friday\n\nBREAKFAST : Moong fry, BBJO, Chocos\n\nLUNCH : Chana masala, DRR, Buttermilk, Fruit\n\nTIFFIN : Masala Dosa\n\nDINNER : Kadai paneer, DRR, Cold drink, Chicken Biryani')

        elif body.lower() == 'sa':
            message.reply('22 Feb : Saturday\n\nBREAKFAST : Mix veg paratha, Boiled egg, Curd, Cornflakes, Matar Currey, Schezwan chutney\n\nLUNCH : Methi Puri, matar paneer, Veg raita, veg Pulao, Shrikhand\n\nTIFFIN : Misal Pav, Plain Bournvita\n\nDINNER : Hariyali kabab masala, Dal-roti, Tomato rice')

        elif body.lower() == 'su':
            message.reply('23 Feb : Sunday\n\nBREAKFAST : Green peas paratha, Boiled egg, Curd, Cornflakes, Schezwan chutney\n\nLUNCH : Aloo Tomato, Kadi-Khichdi, Dahi, Roti, Rasna\n\nTIFFIN : Pani Puri, Plain Bournvita\n\nDINNER : Veg makkhanwala, Egg bhurji, DRR, Shrikhand')

        else :
            message.reply('Invalid query!! Enter the first two letters of the day of the week. For example, enter `sa` for Saturday\'s menu.')

application = webapp.WSGIApplication([('/_ah/xmpp/message/chat/', XMPPHandler)],
                                     debug=True)
 
def main():
    run_wsgi_app(application)
 
if __name__ == "__main__":
    main()
